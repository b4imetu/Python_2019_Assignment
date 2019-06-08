# -*- coding: utf-8 -*-
# Project 2 飞机大战游戏 Shot Them Up! Deluxe Version
# 环境要求：pygame

import pygame
import random
from os import path

image_dir = path.join(path.dirname(__file__),'image')
sound_dir = path.join(path.dirname(__file__),'sound')

WIDTH = 900
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Shot Them Up! Deluxe Version")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

def draw_text(surface, text, size, x, y): #显示文字
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def draw_lives(surface,x,y,lives,image): #显示生命数
    for i in range(lives):
        image_rect = image.get_rect()
        image_rect.x = x+30*i
        image_rect.y = y
        surface.blit(image,image_rect)

def draw_healthbar(surface,x, y, pct): #画血量条
    if pct < 0:
        pct = 0;
    BAR_LENGTH = 500
    BAR_HEIGHT = 10
    fill = (pct / 100)*BAR_LENGTH
    outline_rect = pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect = pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surface,GREEN,fill_rect)
    pygame.draw.rect(surface,WHITE,outline_rect,2)
	
def show_go_screen(): #显示游戏开始界面
    screen.blit(background,background_rect)
    draw_text(screen,'SHOT THEM UP!',48,WIDTH/2,HEIGHT/4)
    draw_text(screen,'Arrow keys ←→ to MOVE',22,WIDTH/2,HEIGHT/2-25)
    draw_text(screen,'Space key to FIRE',22,WIDTH/2,HEIGHT/2+25)
    draw_text(screen,'Press any key to begin',18,WIDTH/2,HEIGHT*3/4-25)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_image,(50,38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.radius = 20
        self.health = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 2
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        # timeout for powerups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        # unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH/2
            self.rect.bottom = HEIGHT-10

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx -= 5
        if keystate[pygame.K_RIGHT]:
            self.speedx += 5
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx,self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if self.power >= 2:
                bullet1 = Bullet(self.rect.left,self.rect.centery)
                bullet2 = Bullet(self.rect.right,self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH/2,HEIGHT+200)


# 陨石类
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orin = random.choice(meteor_images)
        self.image_orin.set_colorkey(BLACK)
        self.image = self.image_orin.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH-self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-3,3)
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rot = 0
        self.rot_speed = random.randrange(-8,8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orin,self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH-self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)

# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_image
        self.image.set_colorkey()
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# 辅助道具、能力增强类
class Pow(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['health','gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom > HEIGHT:
            self.kill()

# 加载游戏图形资源
background = pygame.image.load(path.join(image_dir,'background.png')).convert()
background_rect = background.get_rect()
player_image = pygame.image.load(path.join(image_dir,'playerShip1_orange.png')).convert()
player_mini_image = pygame.transform.scale(player_image,(25,19))
player_mini_image.set_colorkey(BLACK)
bullet_image = pygame.image.load(path.join(image_dir,'laserBullet.png')).convert()
meteor_images = []
meteor_list = ['meteorBrown_med1.png','meteorBrown_med3.png','meteorBrown_small1.png',
                'meteorBrown_small2.png','meteorBrown_tiny1.png','meteorBrown_tiny2.png']
for image in meteor_list:
    meteor_images.append(pygame.image.load(path.join(image_dir,image)).convert())

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    image = pygame.image.load(path.join(image_dir,filename)).convert()
    image.set_colorkey(BLACK)
    image_lg = pygame.transform.scale(image,(75,75))
    explosion_anim['lg'].append(image_lg)
    image_sm = pygame.transform.scale(image,(32,32))
    explosion_anim['sm'].append(image_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    image = pygame.image.load(path.join(image_dir,filename)).convert()
    image.set_colorkey(BLACK)
    explosion_anim['player'].append(image)
powerup_images = {}
powerup_images['health'] = pygame.image.load(path.join(image_dir,'health_gold.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(image_dir,'bolt_gold.png')).convert()

# Load all game sounds
shoot_sound = pygame.mixer.Sound(path.join(sound_dir,'laser_shoot.wav'))
health_sound = pygame.mixer.Sound(path.join(sound_dir,'health.wav'))
power_sound = pygame.mixer.Sound(path.join(sound_dir,'powerup.wav'))
expl_sounds = []
for sound in ['explosion9.wav','explosion.wav','explosion10.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(sound_dir,sound)))
player_dir_sound = pygame.mixer.Sound(path.join(sound_dir,'rumble1.ogg'))
pygame.mixer.music.load(path.join(sound_dir,'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play(loops=-1)
# Game loop 游戏循环
game_over = True
running = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            newmob()

        score = 0
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input(events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()

    # check to see if a bullet hit a mobs
    hits = pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit in hits:
        score += 50 - hit.radius
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center,'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            power = Pow(hit.rect.center)
            all_sprites.add(power)
            powerups.add(power)
        newmob()

    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player,mobs,True,pygame.sprite.collide_circle)
    for hit in hits:
        player.health -= hit.radius * 2
        expl_sounds[2].play()
        expl = Explosion(hit.rect.center,'sm')
        all_sprites.add(expl)
        newmob()
        if player.health <= 0:
            player_dir_sound.play()
            death_explosion = Explosion(player.rect.center,'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.health = 100

    # check to see if player hit a powerup
    hits = pygame.sprite.spritecollide(player,powerups,True)
    for hit in hits:
        if hit.type == 'health':
            health_sound.play()
            player.health += random.randrange(10,30)
            if player.health >= 100:
                player.health = 100
        if hit.type == 'gun':
            power_sound.play()
            player.powerup()

    # if the player died and the explosion has finished playing
    if player.lives == 0 and not death_explosion.alive():
        game_over = True

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    draw_text(screen, "SCORE: "+str(score), 20, WIDTH/2, 25)
    draw_healthbar(screen,200,5,player.health)
    draw_lives(screen,WIDTH-100,5,player.lives,player_mini_image)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()