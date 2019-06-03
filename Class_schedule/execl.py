# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'execl.ui'
#
# Created: Sun Jun 02 21:26:45 2019
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!
# 环境要求：PyQt5
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication

class MyComboBox(QtWidgets.QComboBox):      #新建自己的一个类
    popupAboutToBeShown = pyqtSignal()      #创建一个信号
    def mousePressEvent(self, QMouseEvent): #重写鼠标点击事件
        self.clear()
        self.popupAboutToBeShown.emit()
        self.showPopup()

def get_data_by_file():                     #读取文件信息
    data = [[0] * 6 for _ in range(12)]
    print(data)
    with open('C:/Users/b4ime/Desktop/Class_schedule/curriculum.txt', 'r') as f1:
        lists = f1.readlines()
    for i in range(1,len(lists)):
        list = lists[i].split()
        print("%s %s"%(i,list))
        #print(list)
        for j in range(1,6):
            data[i][j]=list[j]
    return data

def get_time_by_index(index):   #获取上课时间
    data = "8:00-8:50"
    if index==1:
        data = "8:00-8:50"
    if index == 2:
        data = "9:00-9:50"
    if index == 3:
        data = "10:00-10:50"
    if index == 4:
        data = "11:00-11:50"
    if index == 5:
        data = "13:30-14:20"
    if index == 6:
        data = "14:30-15:20"
    if index == 7:
        data = "15:30-16:20"
    if index == 8:
        data = "16:30-17:20"
    if index == 9:
        data = "17:30-18:20"
    if index == 10:
        data = "18:30-19:20"
    if index == 11:
        data = "19:30-20:20"
    return data

def get_lists_by_data(data):    #以一维数组保存数据
    lists = []
    for i in range(1, 12):
        for j in range(1, 6):
            list = {"week":j,"index":i,"name":data[i][j]}
            lists.append(list)
    return lists

class Ui_MainWindow(QMainWindow):  #界面类

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # self.setFont(QFont('微软雅黑', 8))
        self.setupUi(self)
        self.retranslateUi(self)
        self.data = get_data_by_file()
        #self.lists = get_lists_by_data()

    def setupUi(self, MainWindow):#添加界面组件
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setFixedSize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 601, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.Tab1 = QtWidgets.QWidget()
        self.Tab1.setObjectName("Tab1")

        self.label = QtWidgets.QLabel(self.Tab1)
        self.label.setGeometry(QtCore.QRect(60, 30, 54, 12))
        self.label.setObjectName("label")

        self.label_1 = QtWidgets.QLabel(self.Tab1)
        self.label_1.setGeometry(QtCore.QRect(60, 70, 80, 20))
        self.label_1.setObjectName("label_1")

        self.lineEdit_1 = QtWidgets.QLineEdit(self.Tab1)
        self.lineEdit_1.setGeometry(QtCore.QRect(150, 70, 80, 20))
        self.lineEdit_1.setObjectName("lineEdit_1")

        self.pushButton_3 = QtWidgets.QPushButton(self.Tab1)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 67, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.check_by_class)


        self.comboBox = QtWidgets.QComboBox(self.Tab1)
        self.comboBox.setGeometry(QtCore.QRect(120, 20, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")



        self.label_2 = QtWidgets.QLabel(self.Tab1)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 54, 12))
        self.label_2.setObjectName("label_2")

        self.comboBox_2 = MyComboBox(self.Tab1)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 20, 81, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.popupAboutToBeShown.connect(self.update_combobox2)




        self.pushButton = QtWidgets.QPushButton(self.Tab1)
        self.pushButton.setGeometry(QtCore.QRect(420, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.check_by_thin)

        self.textEdit = QtWidgets.QTextEdit(self.Tab1)
        self.textEdit.setGeometry(QtCore.QRect(0,100, 591, 311))
        self.textEdit.setObjectName("textEdit")


        self.tabWidget.addTab(self.Tab1, "")
        self.tab_2 = QtWidgets.QWidget()

        self.tab_2.setObjectName("tab_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 50, 591, 311))
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 10, 81, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(170, 20, 54, 12))
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_4.setGeometry(QtCore.QRect(210, 10, 81, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(310, 20, 54, 12))
        self.label_5.setObjectName("label_5")

        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(350, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.check_by_compre)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def check_by_compre(self): #组合查询   依次筛选出发货逻辑的
        self.textEdit_2.clear()
        #获取选项
        choose1 = self.comboBox_3.currentIndex()
        choose2 = self.comboBox_4.currentIndex()
        choose3 = self.lineEdit.text()

        lists = get_lists_by_data(self.data)
        info = "      %20s  %20s %20s %20s" % ("课程名", "星期几", "第几节", "上课时间")
        self.textEdit_2.append(info)

        #三次筛选   三个参数
        list_1 = []
        if  choose1:
            print("1")
            for i in lists:
                if i["week"]==choose1:
                    list_1.append(i)
        else:
            print("2")
            for i in lists:
                list_1.append(i)

        list_2 = []
        if  choose2:
            print("1")
            for i in list_1:
                if i["index"] == choose2:
                    list_2.append(i)
        else:
            print("2")
            for i in list_1:
                list_2.append(i)

        list_3 = []
        if choose3!="":
            print("1")
            #choose = choose3
            for i in list_2:
                if i["name"] == choose3:
                    list_3.append(i)
        else:
            print("2")
            #choose = "未指定"
            for i in list_2:
                list_3.append(i)


        #展示
        for i in list_3:
            index = "第%s节" % i["index"]
            week = "星期%s" % i["week"]

            info = "%20s  %20s %20s %20s" % (i["name"], week, index, get_time_by_index(i["index"]))
            self.textEdit_2.append(info)


    def check_by_class(self):#通过课程名查询
        self.textEdit.clear()
        choose = self.lineEdit_1.text()
        if choose=="":
            return
        print(choose)
        info = "      %20s  %20s %20s %20s" % ("课程名","星期几", "第几节", "上课时间")
        self.textEdit.append(info)
        for i in range(1, 12):
            for j in range(1,6):
                if self.data[i][j]==choose:
                    index = "第%s节" % i
                    week = "星期%s"%j
                    info = "%20s  %20s %20s %20s" % (str(choose),week, index, get_time_by_index(i))
                    self.textEdit.append(info)
        print("456")

    def check_by_thin(self):#普通查询   星期  节次 上课时间
        self.textEdit.clear()

        choose_1 = self.comboBox.currentIndex()
        choose_2 = self.comboBox_2.currentIndex()+1
        if choose_1==0:  #查询星期几的课程
            info = "     %30s %30s %30s"%("课程名","第几节","上课时间")
            self.textEdit.append(info)
            for i in range(1,12):
                index = "第%s节"%i
                info = "%30s %30s %30s"%(self.data[i][choose_2],index,get_time_by_index(i))
                self.textEdit.append(info)

        elif choose_1==1:#查询第几节的课程
            info = "     %30s %30s %30s" % ("课程名", "星期", "上课时间")
            self.textEdit.append(info)
            for i in range(1, 6):
                index = "星期%s" % i
                info = "%30s %30s %30s" % (self.data[choose_2][i], index, get_time_by_index(choose_2))
                self.textEdit.append(info)
        else:#查上课时间
            info = "           第%s节课的上课时间是：%s"%(choose_2,get_time_by_index(choose_2))
            self.textEdit.append(info)





        print("123")

    def update_combobox2(self):   #根据第一个选择   更新第二个选项
        _translate = QtCore.QCoreApplication.translate
        choose = self.comboBox.currentIndex()
        if choose ==0:
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(0, _translate("MainWindow", "星期一"))
            self.comboBox_2.setItemText(1, _translate("MainWindow", "星期二"))
            self.comboBox_2.setItemText(2, _translate("MainWindow", "星期三"))
            self.comboBox_2.setItemText(3, _translate("MainWindow", "星期四"))
            self.comboBox_2.setItemText(4, _translate("MainWindow", "星期五"))
            print("星期")
        else:
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")

            self.comboBox_2.setItemText(0, _translate("MainWindow", "第一节"))
            self.comboBox_2.setItemText(1, _translate("MainWindow", "第二节"))
            self.comboBox_2.setItemText(2, _translate("MainWindow", "第三节"))
            self.comboBox_2.setItemText(3, _translate("MainWindow", "第四节"))
            self.comboBox_2.setItemText(4, _translate("MainWindow", "第五节"))
            self.comboBox_2.setItemText(5, _translate("MainWindow", "第六节"))
            self.comboBox_2.setItemText(6, _translate("MainWindow", "第七节"))
            self.comboBox_2.setItemText(7, _translate("MainWindow", "第八节"))
            self.comboBox_2.setItemText(8, _translate("MainWindow", "第九节"))
            self.comboBox_2.setItemText(9, _translate("MainWindow", "第十节"))
            self.comboBox_2.setItemText(10, _translate("MainWindow", "第十一节"))
            print("节数")


    def retranslateUi(self, MainWindow):  #组件的名称
        _translate = QtCore.QCoreApplication.translate

        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, _translate("MainWindow", "星期一"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "星期二"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "星期三"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "星期四"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "星期五"))

        MainWindow.setWindowTitle(_translate("MainWindow", "2017-2018第二学年课程表"))

        self.label.setText(_translate("MainWindow", "查询条件："))
        self.comboBox.setItemText(0, _translate("MainWindow", "星期"))
        self.comboBox.setItemText(1, _translate("MainWindow", "第几节"))
        self.comboBox.setItemText(2, _translate("MainWindow", "上课时间"))

        self.label_1.setText(_translate("MainWindow", "按课程名查询："))

        self.label_2.setText(_translate("MainWindow", "查询键值："))

        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab1), _translate("MainWindow", "简单查询"))
        self.label_3.setText(_translate("MainWindow", "星期："))
        self.comboBox_3.setItemText(0, _translate("MainWindow", ""))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "星期一"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "星期二"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "星期三"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "星期四"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "星期五"))
        self.label_4.setText(_translate("MainWindow", "节数："))
        self.comboBox_4.setItemText(0, _translate("MainWindow", ""))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "第一节"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "第二节"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "第三节"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "第四节"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "第五节"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "第六节"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "第七节"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "第八节"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "第九节"))
        self.comboBox_4.setItemText(10, _translate("MainWindow", "第十节"))
        self.comboBox_4.setItemText(11, _translate("MainWindow", "第十一节"))
        self.label_5.setText(_translate("MainWindow", "课程："))
        self.pushButton_2.setText(_translate("MainWindow", "查询"))
        self.pushButton_3.setText(_translate("MainWindow", "查询"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "综合查询"))

def main():  #主函数
    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()