# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FantasyCricketNew.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import sqlite3
from Evaluate_Score import Ui_Dialog
#from Dialog_Save import Ui_Dialog
Match=sqlite3.connect('Match.db')
Teams=sqlite3.connect('Teams.db')
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 458)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 761, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 130, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 150, 361, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 190, 361, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 270, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(440, 190, 371, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 156, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(550, 150, 231, 31))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 22))
        self.menubar.setObjectName("menubar")
        self.menuManageTeams = QtWidgets.QMenu(self.menubar)
        self.menuManageTeams.setObjectName("menuManageTeams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.menuManageTeams.addAction(self.actionNEW_Team)
        self.menuManageTeams.addAction(self.actionOPEN_Team)
        self.menuManageTeams.addAction(self.actionSAVE_Team)
        self.menuManageTeams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManageTeams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menubar.triggered[QtWidgets.QAction].connect(self.menufunction)
        self.radioButton_3.pressed.connect(self.batsmen)
        self.radioButton_4.pressed.connect(self.bowlers)
        self.radioButton_2.pressed.connect(self.allrounders)
        self.radioButton.pressed.connect(self.wicketkeepers)

        #to populate the right list
        self.listWidget.itemDoubleClicked.connect(self.removelist1)
        self.listWidget_2.itemDoubleClicked.connect(self.removelist2) 

        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Batsmen(BAT)   ##"))
        self.label_4.setText(_translate("MainWindow", "Bowlers(BOW) ##"))
        self.label_3.setText(_translate("MainWindow", "Allrounders(AR) ##"))
        self.label.setText(_translate("MainWindow", "Wicket-Keepers(WK) ##"))
        self.label_5.setText(_translate("MainWindow", "Points Available"))
        self.label_6.setText(_translate("MainWindow", "Points Used"))
        self.label_7.setText(_translate("MainWindow", "Your Selection"))
        self.radioButton_3.setText(_translate("MainWindow", "BAT"))
        self.radioButton_4.setText(_translate("MainWindow", "BOW"))
        self.radioButton_2.setText(_translate("MainWindow", "AR"))
        self.radioButton.setText(_translate("MainWindow", "WK"))
        self.label_9.setText(_translate("MainWindow", ">"))
        self.label_8.setText(_translate("MainWindow", "Team Name"))
        self.menuManageTeams.setTitle(_translate("MainWindow", "ManageTeams"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))


    def menufunction(self,action):
        txt=(action.text())
        if txt=='NEW Team':
            root=Tk()
            w=Label(root,text="My Program")
            w.pack()
            team=tkinter.simpledialog.askstring("Team Name","Enter the name")
            self.label_10.setText(team)
            
        if txt=='SAVE Team':
            if(self.listWidget_2.count()<11 or self.listWidget_2.count()>11):
                root=Tk()
                w=Label(root,text="My Program")
                w.pack()
                tkinter.messagebox.showinfo("Try Again","Number of Players should be 11")
            elif(self.label_10.text()==''):
                root=Tk()
                w=Label(root,text="My Program")
                w.pack()
                tkinter.messagebox.showinfo("Required*","Set a name first!!")
                
            else:
                items = []
                players = []
                val1 = []
                val2 = []
                totalValue=0
                teamName=self.label_10.text()
                for index in range(self.listWidget_2.count()):
                    items.append(self.listWidget_2.item(index))
                for i in range(len(items)):
                    players.append(items[i].text())
                for i in range(len(players)):
                    sql="select Value from MyPlayers where Player='"+players[i]+"';"
                    cur=Match.cursor()
                    cur.execute(sql)
                    val=cur.fetchone()
                    val1.append(val)
                for i in range(len(val1)):
                    totalValue+=int(val1[i][0])
                mycursor=Teams.cursor()
                sql="insert into TeamFormed(Name,Players,Value) VALUES(?,?,?);"
                mycursor.execute(sql,(teamName,str(players),str(totalValue)))
                Teams.commit()
                root=Tk()
                w=Label(root,text="My Program")
                w.pack()
                tkinter.messagebox.showinfo("Congratulations!!!","Team saved successfully!!")

        if txt=='EVALUATE Team':
            self.eval()
            
    def eval(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


    def batsmen(self):
        items = []
        list2 = []
        list1 = []
        sql="select Player from MyPlayers where Designation='Bat';"
        cur=Match.cursor()
        cur.execute(sql)
        batters=cur.fetchall()
        num=len(batters)
        self.label_2.setText("Batsmen(BAT)  "+str(num))
        for index in range(self.listWidget_2.count()):
                items.append(self.listWidget_2.item(index))
        if len(items)==0:
            #self.label_2.setText("Batsmen(BAT)  "+str(num))
            self.listWidget.clear()
            for i in range(len(batters)):
                item=batters[i][0]
                self.listWidget.addItem(item)
        else:
            for i in range(len(items)):
                list2.append(items[i].text())
            #self.label_2.setText("Batsmen(BAT)  "+str(num-len(items)))
            self.listWidget.clear()
            for i in range(len(batters)):
                list1.append(batters[i][0])
            l3 = [x for x in list1 if x not in list2]
            for i in range(len(l3)):
                list4=l3[i]
                self.listWidget.addItem(list4)
                
            
            
            
            

    def bowlers(self):
        items = []
        list2 = []
        list1 = []
        sql="select Player from MyPlayers where Designation='Bowl';"
        cur=Match.cursor()
        cur.execute(sql)
        bowl=cur.fetchall()
        num=len(bowl)
        self.label_4.setText("Bowlers(BOW)  "+str(num))
        for index in range(self.listWidget_2.count()):
                items.append(self.listWidget_2.item(index))
        if len(items)==0:
            #self.label_4.setText("Bowlers(BOW)  "+str(num))
            self.listWidget.clear()
            for i in range(len(bowl)):
                item=bowl[i][0]
                self.listWidget.addItem(item)
        else:
            for i in range(len(items)):
                list2.append(items[i].text())
            #self.label_4.setText("Bowlers(BOW)  "+str(num-len(items)))
            self.listWidget.clear()
            for i in range(len(bowl)):
                list1.append(bowl[i][0])
            l3 = [x for x in list1 if x not in list2]
            for i in range(len(l3)):
                list4=l3[i]
                self.listWidget.addItem(list4)

    def allrounders(self):
        items = []
        list2 = []
        list1 = []
        sql="select Player from MyPlayers where Designation='AR';"
        cur=Match.cursor()
        cur.execute(sql)
        allround=cur.fetchall()
        num=len(allround)
        self.label_3.setText("Allrounders(AR)  "+str(num))
        for index in range(self.listWidget_2.count()):
                items.append(self.listWidget_2.item(index))
        if len(items)==0:
            #self.label_3.setText("Allrounders(AR)  "+str(num))
            self.listWidget.clear()
            for i in range(len(allround)):
                item=allround[i][0]
                self.listWidget.addItem(item)
        else:
            for i in range(len(items)):
                list2.append(items[i].text())
            #self.label_3.setText("Allrounders(AR)  "+str(num-len(items)))
            self.listWidget.clear()
            for i in range(len(allround)):
                list1.append(allround[i][0])
            l3 = [x for x in list1 if x not in list2]
            for i in range(len(l3)):
                list4=l3[i]
                self.listWidget.addItem(list4)
    def wicketkeepers(self):
        items = []
        list2 = []
        list1 = []
        sql="select Player from MyPlayers where Designation='WK';"
        cur=Match.cursor()
        cur.execute(sql)
        wk=cur.fetchall()
        num=len(wk)
        self.label.setText("Wicket-Keepers(WK)  "+str(num))
        for index in range(self.listWidget_2.count()):
                items.append(self.listWidget_2.item(index))
        if len(items)==0:
            #self.label.setText("Wicket-Keepers(WK)  "+str(num))
            self.listWidget.clear()
            for i in range(len(wk)):
                item=wk[i][0]
                self.listWidget.addItem(item)
        else:
            for i in range(len(items)):
                list2.append(items[i].text())
            #self.label.setText("Wicket-Keepers(WK)  "+str(num-len(items)))
            self.listWidget.clear()
            for i in range(len(wk)):
                list1.append(wk[i][0])
            l3 = [x for x in list1 if x not in list2]
            for i in range(len(l3)):
                list4=l3[i]
                self.listWidget.addItem(list4)
        
        

    def removelist1(self,item):
        items = []
        des1 = []
        for index in range(self.listWidget_2.count()):
                items.append(self.listWidget_2.item(index))
        if len(items)==0:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            
        else:
            self.listWidget.takeItem(self.listWidget.row(item))
            sql="select Designation from MyPlayers where Player='"+item.text()+"';"
            cur=Match.cursor()
            cur.execute(sql)
            desig=cur.fetchone()
            for i in range(len(items)):
                sql="select Designation from MyPlayers where Player='"+items[i].text()+"';"
                cur=Match.cursor()
                cur.execute(sql)
                des=cur.fetchone()
                des1.append(des)
            count=0
            if desig[0]=='WK':
                for j in range(len(des1)):
                    if des1[j][0]==desig[0]:
                        count+=1        
                if(count>=1):
                    root=Tk()
                    w=Label(root,text="My Program")
                    w.pack()
                    tkinter.messagebox.showinfo("Try Again","You can have only one WK")
                else:
                    self.listWidget.takeItem(self.listWidget.row(item))
                    self.listWidget_2.addItem(item.text())
                    
            else:
                self.listWidget.takeItem(self.listWidget.row(item))
                self.listWidget_2.addItem(item.text())
            
                


    def removelist2(self, item):
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        self.listWidget.addItem(item.text())

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
