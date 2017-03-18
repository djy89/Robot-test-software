# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\eric\ys01\ui\P1P5.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from __future__ import division
from math import sqrt
import numpy as np

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(828, 599)
        Dialog.setSizeGripEnabled(True)
        self.stackedWidget_3 = QtGui.QStackedWidget(Dialog)
        self.stackedWidget_3.setGeometry(QtCore.QRect(220, 50, 541, 491))
        self.stackedWidget_3.setObjectName(_fromUtf8("stackedWidget_3"))
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.label_17 = QtGui.QLabel(self.page_7)
        self.label_17.setGeometry(QtCore.QRect(60, 30, 111, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.widget = QtGui.QWidget(self.page_7)
        self.widget.setGeometry(QtCore.QRect(90, 110, 322, 193))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_18 = QtGui.QLabel(self.widget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_8.addWidget(self.label_18)
        self.label_19 = QtGui.QLabel(self.widget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_8.addWidget(self.label_19)
        self.label_20 = QtGui.QLabel(self.widget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_8.addWidget(self.label_20)
        self.label_21 = QtGui.QLabel(self.widget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_8.addWidget(self.label_21)
        self.label_22 = QtGui.QLabel(self.widget)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_8.addWidget(self.label_22)
        self.label_23 = QtGui.QLabel(self.widget)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout_8.addWidget(self.label_23)
        self.label_24 = QtGui.QLabel(self.widget)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.verticalLayout_8.addWidget(self.label_24)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem7)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem8)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem9)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem10)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem11)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem12)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem13)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.RR = QtGui.QLineEdit(self.widget)
        self.RR.setObjectName(_fromUtf8("RR"))
        self.verticalLayout_7.addWidget(self.RR)
        self.rr = QtGui.QLineEdit(self.widget)
        self.rr.setObjectName(_fromUtf8("rr"))
        self.verticalLayout_7.addWidget(self.rr)
        self.zz1 = QtGui.QLineEdit(self.widget)
        self.zz1.setObjectName(_fromUtf8("zz1"))
        self.verticalLayout_7.addWidget(self.zz1)
        self.hh = QtGui.QLineEdit(self.widget)
        self.hh.setObjectName(_fromUtf8("hh"))
        self.verticalLayout_7.addWidget(self.hh)
        self.dd = QtGui.QLineEdit(self.widget)
        self.dd.setObjectName(_fromUtf8("dd"))
        self.verticalLayout_7.addWidget(self.dd)
        self.zz = QtGui.QLineEdit(self.widget)
        self.zz.setObjectName(_fromUtf8("zz"))
        self.verticalLayout_7.addWidget(self.zz)
        self.xx = QtGui.QLineEdit(self.widget)
        self.xx.setObjectName(_fromUtf8("xx"))
        self.verticalLayout_7.addWidget(self.xx)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.stackedWidget_3.addWidget(self.page_7)
        self.page_8 = QtGui.QWidget()
        self.page_8.setObjectName(_fromUtf8("page_8"))
        self.label_25 = QtGui.QLabel(self.page_8)
        self.label_25.setGeometry(QtCore.QRect(70, 50, 111, 16))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label = QtGui.QLabel(self.page_8)
        self.label.setGeometry(QtCore.QRect(70, 130, 16, 161))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(self.page_8)
        self.textEdit.setGeometry(QtCore.QRect(150, 120, 361, 192))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.page_8)
        self.pushButton.setGeometry(QtCore.QRect(240, 390, 92, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.page_8)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 390, 92, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.stackedWidget_3.addWidget(self.page_8)
        self.toolBox = QtGui.QToolBox(Dialog)
        self.toolBox.setGeometry(QtCore.QRect(80, 160, 121, 145))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 121, 85))
        self.page.setObjectName(_fromUtf8("page"))
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 121, 85))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.stackedWidget_3.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.toolBox, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), self.stackedWidget_3.setCurrentIndex)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.activeparameter)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.calcutlate)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_17.setText(_translate("Dialog", "1.輸入參數", None))
        self.label_18.setText(_translate("Dialog", "R", None))
        self.label_19.setText(_translate("Dialog", "r", None))
        self.label_20.setText(_translate("Dialog", "z1", None))
        self.label_21.setText(_translate("Dialog", "h", None))
        self.label_22.setText(_translate("Dialog", "d6", None))
        self.label_23.setText(_translate("Dialog", "Z(MP)", None))
        self.label_24.setText(_translate("Dialog", "X(MP)", None))
        self.RR.setText(_translate("Dialog", "730", None))
        self.rr.setText(_translate("Dialog", "90", None))
        self.zz1.setText(_translate("Dialog", "244.2", None))
        self.hh.setText(_translate("Dialog", "510", None))
        self.dd.setText(_translate("Dialog", "170", None))
        self.zz.setText(_translate("Dialog", "70.57", None))
        self.xx.setText(_translate("Dialog", "0", None))
        self.label_25.setText(_translate("Dialog", "2.計算測量點", None))
        self.label.setText(_translate("Dialog", "P1\n"
"P2\n"
"P3\n"
"P4\n"
"P5", None))
        self.pushButton.setText(_translate("Dialog", "確認參數", None))
        self.pushButton_2.setText(_translate("Dialog", "計算", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Dialog", "輸入參數", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Dialog", "計算測量點", None))

    def activeparameter(self):
        self.R=float(self.RR.text())
        self.r=float(self.rr.text())
        self.z1=float(self.zz1.text())
        self.h=float(self.hh.text())
        self.d6=float(self.dd.text())
        self.X=float(self.xx.text())
        self.Z=float(self.zz.text())
        print(self.r)
    def calcutlate(self):
        sintheta=(self.r+sqrt((self.r)**2+8*self.R**2))/(4*self.R)
        costheta=sqrt(1-sintheta**2)
        #return six_theta
        x=costheta*float(self.R)
        y=sintheta*float(self.R)-self.r
        #print(sintheta,costheta)
        a=y
        b=2*x
        c=float(self.h)
        C4=np.array([float(self.r),x,float(self.z1)+c])
        C1=C4+np.array([a,0,0])
        C5=C1+np.array([0,0,-c])
        C8=C4+np.array([0,0,-c])
        C3=C4+np.array([0,-b,0])
        C7=C8+np.array([0,-b,0])
        C6=C5+np.array([0,-b,0])
        C2=C1+np.array([0,-b,0])
        P1=(C1+C7)*0.5
        temp=abs(C1-C7)*0.1
        temp1=abs(C2-C8)*0.1
        P2=C1-temp
        P4=C7+temp
        P3=C2+np.array([-temp1[0],temp1[1],-temp1[2]])
        P5=C8+np.array([temp1[0],-temp1[1],temp1[2]])
        temp_xiebian=float(sqrt(y**2+c**2))
        cosbeta=c/temp_xiebian
        sinbeta=a/temp_xiebian
        offsetZ=np.array([float(self.Z+self.d6)*cosbeta,0,-float(self.Z+self.d6)*sinbeta])
        offsetX=np.array([float(self.X)*sinbeta,0,-float(self.X)*cosbeta])
        OP1=P1+offsetZ+offsetX
        OP2=P2+offsetZ+offsetX
        OP3=P3+offsetZ+offsetX
        OP4=P4+offsetZ+offsetX
        OP5=P5+offsetZ+offsetX
        text=str(OP1)+'\n'+str(OP2)+'\n'+str(OP3)+'\n'+str(OP4)+'\n'+str(OP5)
        self.textEdit.setText(text)
#        print(str(OP1))
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
