# Python 大作业

# *Project 1 Curriculum* 课程表实验报告

## 一、实验目的

运用课上所学知识制作实现一个学生👨‍🎓课程表📅

## 二、实验环境

[Python](<https://www.python.org/downloads/release/python-370/>) 3.7.0 + [PyQt5](<https://pypi.org/project/PyQt5/>) 5.12.2

## 三、实验要求

```
（1）将一周内所有课程和时间以如下形式存储到文件curriculum.txt中

星期        星期 1        星期2        星期3        星期4        星期5
第一节        Xxx        xxx        xxx        xxx        xxx
第二节        Xxx        xxx        xxx        xxx        xxx
第三节        Xxx        xxx        xxx        xxx        xxx
第四节        Xxx        xxx        xxx        xxx        xxx
第五节        Xxx        xxx        xxx        xxx        xxx
第六节        Xxx        xxx        xxx        xxx        xxx
第七节        Xxx        xxx        xxx        xxx        xxx
第八节        Xxx        xxx        xxx        xxx        xxx
第九节        Xxx        xxx        xxx        xxx        xxx
第十节        Xxx        xxx        xxx        xxx        xxx
第十一节        Xxx        xxx        xxx        xxx        xxx

（2）程序启动后首先解析文件，将内容存储到数据结构中。

（3）使用GUI编程，满足标题显示xxx班某某学期-某某学期课程表,例如2017-2018第二学年课程表
查询条件：星期，第几节，课程名
	如果查询星期，应显示这一天下所有课程：课程名，第几节，上课时间
	如果查询第几节，应该显示所有天的这一节：课程名，第几节，上课时间
	如果查询课程名，应显示课程名，星期几，第几节，上课时间（若有多次，则都显示）
	如果综合查询，必须给出满足多个查询条件的信息：课程名，星期几，第几节，上课时间
	也可单独查询上课时间：例如查询第一节时间，应给出上午8:008:50，等等
```

## 四、实验过程

在课上学习了python中的Tkinter组件后，我们去深入了解了python中实现GUI编程的各种常用框架。经过比较，我们发现Tkinter框架具有比较大的局限性，需要靠自己实现全部的UI布局，并且显示效果也比较单一。于是我们找到了**PyQt5**框架，它显示效果基于本地系统，泛用性强，开发文档也很丰富，有多样的显示效果，布局也十分方便。基于此，我们决定借助PyQt5框架实现大作业中的“学生课程表”任务。

我们首先借助pyqt5-tools中的desigher工具完成了主程序界面的设计，将生成的窗口类导入到了程序文件中，解决了界面设计的难题；接着我们写了一些与文件读写操作相关的函数和类，还写了判断时间段的函数；我们还完善了根据课程名查询，各种参数的普通查询以及组合查询的函数代码，它们都是直接在存储课程表数据的数组中进行查找的。之后我们封装了主循环中进行的具体操作为一个main()函数，在把它放到主循环中即完成设计。

## 五、实验结果

最终，我们完成了一款飞行射击游戏。玩家操作飞机在窗口底端左右移动，并可从下向上发射子弹，窗口顶端随机刷新射向下方不同方向的速度、大小均不同的石块；玩家子弹击中石块可使其爆炸以消灭之，并有几率随机出现增强玩家火力或护盾的道具；玩家若被石块集中会根据石块的大小扣减护盾值，护盾值归零即损失一条生命，一局游戏中玩家总共有三条生命，损失殆尽时游戏结束。

#### 效果截图

我们按照要求实现了一个课程表查询程序，能够读取课程表文件信息并存入堆栈；能够根据不同的星期几、第几节课、课程名称分别查询；还能够查询每节课的上课时间；同时也能按要求进行星期几、节数、课程名的组合查询。

![效果截图1](<https://github.com/b4imetu/Python_2019_Assignment/raw/master/capture/Curriculum (1).jpg>)

![效果截图2](<https://github.com/b4imetu/Python_2019_Assignment/raw/master/capture/Curriculum (2).jpg>)

![效果截图3](<https://github.com/b4imetu/Python_2019_Assignment/raw/master/capture/Curriculum (3).jpg>)

![效果截图4](<https://github.com/b4imetu/Python_2019_Assignment/raw/master/capture/Curriculum (4).jpg>)

![效果截图5](<https://github.com/b4imetu/Python_2019_Assignment/raw/master/capture/Curriculum (5).jpg>)

## 六、遇到的问题与解决方法

一开始我们没有学会使用designer工具而是完全靠自己设计界面UI，十分耗时且效果不好，出了错误也难以修改，后来学会使用designer才能完全发挥PyQt5的能力，方便快捷地完成了界面设计。

曾经我们在主循环中不能正常对窗口发出关闭指令，更改exit中参数才解决。

曾经程序中的按钮点按后不会向消息槽中送入消息，我们上网寻找建议和解决办法，最终我们不得不针对按钮重写鼠标点击事件才解决问题。

我们在编写各种查询方法时遇到了很多逻辑问题，这促使我们把课程表改为在堆栈中以二维数组存储，改进了存储结构，才方便地解决问题。

我们在读取文件时还曾经忘记了使用utf-8编码导致出现乱码，改变编码方式后解决。