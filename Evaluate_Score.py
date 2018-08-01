# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluate_Score.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Score_Calculator import scored
import sqlite3
import ast
Teams=sqlite3.connect('Teams.db')
Match=sqlite3.connect('Match.db')
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(656, 483)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 591, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 611, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 130, 611, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 150, 611, 271))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_3.addWidget(self.listWidget_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_3.addWidget(self.listWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 440, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.evaluateScore)

        #For Team Names in Combo Box
        teams = []
        sql="select Name from TeamFormed;"
        cur=Teams.cursor()
        cur.execute(sql)
        team=cur.fetchall()
        for i in range(len(team)):
            teams.append(team[i][0])
        self.comboBox_2.clear()
        self.comboBox_2.addItems(teams)

        #For Matches played in the Combo Box
        matches = []
        sql1="select Matches from MatchesPlayed;"
        curs=Match.cursor()
        curs.execute(sql1)
        match=curs.fetchall()
        for i in range(len(match)):
            matches.append(match[i][0])
        self.comboBox.clear()
        self.comboBox.addItems(matches)

    def evaluateScore(self):
        score = []
        playersSelected = []
        selectedTeam = str(self.comboBox_2.currentText())
        selectedMatch=str(self.comboBox.currentText())
        sql2="select Players from TeamFormed where Name='"+selectedTeam+"';"
        curt=Teams.cursor()
        curt.execute(sql2)
        players=curt.fetchone()
        #Add the player Names of the selected Team
        self.listWidget_2.clear()
        for i in eval(players[0]):
            self.listWidget_2.addItem(i)

        for i in eval(players[0]):
            playersSelected.append(i)
        
        for i in range(len(playersSelected)):
            player=playersSelected[i]
            sql3="select Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,RunOut from '"+selectedMatch+"' where Player='"+player+"';"
            curts=Match.cursor()
            curts.execute(sql3)
            score.append(curts.fetchone())
        self.listWidget.clear()
        for i in range(len(score)):
            score1=score[i]
            points=scored(self,score1)
            self.listWidget.addItem(str(points))
        
            
        

       

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "              Evaluate the Performance of your Fantasy Team"))
        self.pushButton.setText(_translate("Dialog", "Calculate Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

