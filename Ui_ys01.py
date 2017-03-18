# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\eric\ys01\ys01.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from math import cos, sin, radians
import numpy as np

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
        Dialog.resize(933, 727)
        Dialog.setSizeGripEnabled(True)
        self.toolBox = QtGui.QToolBox(Dialog)
        self.toolBox.setGeometry(QtCore.QRect(30, 190, 141, 141))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.button1page = QtGui.QWidget()
        self.button1page.setGeometry(QtCore.QRect(0, 0, 141, 23))
        self.button1page.setObjectName(_fromUtf8("button1page"))
        self.toolBox.addItem(self.button1page, _fromUtf8(""))
        self.button2page = QtGui.QWidget()
        self.button2page.setGeometry(QtCore.QRect(0, 0, 141, 23))
        self.button2page.setObjectName(_fromUtf8("button2page"))
        self.toolBox.addItem(self.button2page, _fromUtf8(""))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 141, 23))
        self.page.setAccessibleName(_fromUtf8(""))
        self.page.setObjectName(_fromUtf8("page"))
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.button3page = QtGui.QWidget()
        self.button3page.setGeometry(QtCore.QRect(0, 0, 141, 22))
        self.button3page.setObjectName(_fromUtf8("button3page"))
        self.toolBox.addItem(self.button3page, _fromUtf8(""))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(390, 20, 221, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_16.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.stackedWidget = QtGui.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 110, 691, 541))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page1 = QtGui.QWidget()
        self.page1.setObjectName(_fromUtf8("page1"))
        self.label = QtGui.QLabel(self.page1)
        self.label.setGeometry(QtCore.QRect(40, 30, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(self.page1)
        self.widget.setGeometry(QtCore.QRect(90, 100, 233, 201))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.a1 = QtGui.QLineEdit(self.widget)
        self.a1.setObjectName(_fromUtf8("a1"))
        self.horizontalLayout.addWidget(self.a1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem1 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.a2 = QtGui.QLineEdit(self.widget)
        self.a2.setObjectName(_fromUtf8("a2"))
        self.horizontalLayout_2.addWidget(self.a2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        spacerItem2 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.a3 = QtGui.QLineEdit(self.widget)
        self.a3.setObjectName(_fromUtf8("a3"))
        self.horizontalLayout_3.addWidget(self.a3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        spacerItem3 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.a4 = QtGui.QLineEdit(self.widget)
        self.a4.setObjectName(_fromUtf8("a4"))
        self.horizontalLayout_4.addWidget(self.a4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        spacerItem4 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.a5 = QtGui.QLineEdit(self.widget)
        self.a5.setObjectName(_fromUtf8("a5"))
        self.horizontalLayout_5.addWidget(self.a5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)
        spacerItem5 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.a6 = QtGui.QLineEdit(self.widget)
        self.a6.setObjectName(_fromUtf8("a6"))
        self.horizontalLayout_6.addWidget(self.a6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.widget1 = QtGui.QWidget(self.page1)
        self.widget1.setGeometry(QtCore.QRect(390, 100, 233, 201))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_10 = QtGui.QLabel(self.widget1)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_7.addWidget(self.label_10)
        spacerItem6 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.d1 = QtGui.QLineEdit(self.widget1)
        self.d1.setObjectName(_fromUtf8("d1"))
        self.horizontalLayout_7.addWidget(self.d1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_11 = QtGui.QLabel(self.widget1)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_8.addWidget(self.label_11)
        spacerItem7 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.d2 = QtGui.QLineEdit(self.widget1)
        self.d2.setObjectName(_fromUtf8("d2"))
        self.horizontalLayout_8.addWidget(self.d2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_12 = QtGui.QLabel(self.widget1)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_9.addWidget(self.label_12)
        spacerItem8 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.d3 = QtGui.QLineEdit(self.widget1)
        self.d3.setObjectName(_fromUtf8("d3"))
        self.horizontalLayout_9.addWidget(self.d3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_13 = QtGui.QLabel(self.widget1)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_10.addWidget(self.label_13)
        spacerItem9 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.d4 = QtGui.QLineEdit(self.widget1)
        self.d4.setObjectName(_fromUtf8("d4"))
        self.horizontalLayout_10.addWidget(self.d4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_14 = QtGui.QLabel(self.widget1)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_11.addWidget(self.label_14)
        spacerItem10 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.d5 = QtGui.QLineEdit(self.widget1)
        self.d5.setObjectName(_fromUtf8("d5"))
        self.horizontalLayout_11.addWidget(self.d5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_15 = QtGui.QLabel(self.widget1)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_12.addWidget(self.label_15)
        spacerItem11 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.d6 = QtGui.QLineEdit(self.widget1)
        self.d6.setObjectName(_fromUtf8("d6"))
        self.horizontalLayout_12.addWidget(self.d6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtGui.QWidget()
        self.page2.setObjectName(_fromUtf8("page2"))
        self.label_2 = QtGui.QLabel(self.page2)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 161, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(self.page2)
        self.textEdit.setGeometry(QtCore.QRect(40, 80, 601, 381))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.page2)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 500, 92, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtGui.QWidget()
        self.page3.setObjectName(_fromUtf8("page3"))
        self.label_3 = QtGui.QLabel(self.page3)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit_2 = QtGui.QTextEdit(self.page3)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 80, 601, 381))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.pushButton_4 = QtGui.QPushButton(self.page3)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 500, 92, 28))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.stackedWidget.addWidget(self.page3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.label_17 = QtGui.QLabel(self.page_4)
        self.label_17.setGeometry(QtCore.QRect(40, 30, 111, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.pushButton = QtGui.QPushButton(self.page_4)
        self.pushButton.setGeometry(QtCore.QRect(430, 500, 92, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.page_4)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 500, 92, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_18 = QtGui.QLabel(self.page_4)
        self.label_18.setGeometry(QtCore.QRect(180, 50, 72, 441))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.textEdit_3 = QtGui.QTextEdit(self.page_4)
        self.textEdit_3.setGeometry(QtCore.QRect(330, 50, 171, 431))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.stackedWidget.addWidget(self.page_4)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.toolBox, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), self.stackedWidget.setCurrentIndex)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.calculate)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit_2.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.activeDHparameter)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "ys01", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.button1page), _translate("Dialog", "輸入DH參數", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.button2page), _translate("Dialog", "輸入變量取值", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Dialog", "輸入絕對誤差", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.button3page), _translate("Dialog", "計算DH誤差", None))
        self.label_16.setText(_translate("Dialog", "YS01 DH誤差識別", None))
        self.label.setText(_translate("Dialog", "1.輸入DH參數", None))
        self.label_4.setText(_translate("Dialog", "a1", None))
        self.a1.setText(_translate("Dialog", "0", None))
        self.label_5.setText(_translate("Dialog", "a2", None))
        self.a2.setText(_translate("Dialog", "365", None))
        self.label_7.setText(_translate("Dialog", "a3", None))
        self.a3.setText(_translate("Dialog", "235", None))
        self.label_6.setText(_translate("Dialog", "a4", None))
        self.a4.setText(_translate("Dialog", "300", None))
        self.label_9.setText(_translate("Dialog", "a5", None))
        self.a5.setText(_translate("Dialog", "0", None))
        self.label_8.setText(_translate("Dialog", "a6", None))
        self.a6.setText(_translate("Dialog", "0", None))
        self.label_10.setText(_translate("Dialog", "d1", None))
        self.d1.setText(_translate("Dialog", "500", None))
        self.label_11.setText(_translate("Dialog", "d2", None))
        self.d2.setText(_translate("Dialog", "N/A", None))
        self.label_12.setText(_translate("Dialog", "d3", None))
        self.d3.setText(_translate("Dialog", "-143.97", None))
        self.label_13.setText(_translate("Dialog", "d4", None))
        self.d4.setText(_translate("Dialog", "0", None))
        self.label_14.setText(_translate("Dialog", "d5", None))
        self.d5.setText(_translate("Dialog", "0", None))
        self.label_15.setText(_translate("Dialog", "d6", None))
        self.d6.setText(_translate("Dialog", "100", None))
        self.label_2.setText(_translate("Dialog", "2.輸入變量取值", None))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    1.3611  428.7575  -42.3855 -137.8667    0.9216 -115.2909</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -3.7460  634.9306   20.0636  113.2854   27.0743  -15.5579</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  135.7375  987.8210   84.0942  -63.0520   76.6613   79.7332</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -52.8689  772.5425   54.6280  -91.3579    7.6534   28.1736</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -18.2003  871.1757  -23.7084  -56.6232  -71.5020    4.8311</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  166.8709  546.6084   41.6198  -44.7508  -11.0656   87.3284</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -164.7728  576.4998  -39.9086   16.7594  -17.3014  -96.5525</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  170.2650  648.5707   93.2286   22.2913  111.8527   97.9325</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -111.8855  415.2732   97.1139  -37.5040   28.8132  -94.0760</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   60.1633  799.2148   67.3954  -36.6729   46.8936    4.0792</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   31.1183  603.1102  -46.6679    5.5322   52.8395  -85.6426</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   63.0405  717.4477  -30.8620   56.7110  -36.7452   14.2489</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -50.0321  446.1965  -80.7951  162.3295    4.0777 -118.9009</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   43.3002  310.9797   48.2615   80.0455   13.6067   64.0037</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  112.0143  580.4583   71.8810  -35.9713  -82.4411   83.6902</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -173.0673  489.9674   79.2908  119.4737   14.8935  100.0371</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -149.8055  830.4907   -6.0116 -131.6382   46.7528  116.8724</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  170.9286  824.2367    3.7283 -158.2320  -17.6507    1.2319</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   54.4858  734.8098 -104.2696 -149.6711   80.7049  -54.8588</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -96.7544  306.8031   75.9312 -120.9966   55.5329  -95.8199</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -34.7432  217.2447  -31.9055  -63.2808  -33.5925    1.8837</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -136.0726  647.8726  -90.6386  -71.3784  -10.9890   20.5462</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -83.3620  440.6552   75.9162 -175.7948  -27.2664   63.0929</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -87.1754  951.5278   43.0205   14.3658   66.1331 -100.0890</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -60.6005  984.7229   71.7967 -145.6658   56.2251   38.7831</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -125.1958  429.2963  -71.6119 -127.2547  -16.7333    4.0750</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -54.7172  840.6562   21.5742   47.2108   46.5006  -78.9485</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -136.2030  916.8891   19.4272  129.3553  106.8512  105.2539</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  138.2951  678.0213 -110.5244  170.7198   68.2158   21.7160</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -146.0598  907.2134  -42.2436   25.5018   49.3372  -14.2477</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  154.8146  954.9852  -73.9311  178.8661  -93.7598  106.0605</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -36.3528  639.3265   32.0007   19.2750  -26.4166   37.4193</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -162.9355  782.7095  -71.9877    5.5650   21.8171  -11.5330</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -56.7455  661.4066   75.0877  -60.9545   -9.7488   81.5274</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   84.9478  220.6860   58.3789  -25.1994 -107.9184    7.8296</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  106.0856  557.2248  -46.3936   -2.9497  -65.1150   12.9329</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   16.1661  717.0416  -20.5033 -154.4266   80.2054   43.2157</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   67.0404  616.9624   26.7532  139.5861 -116.2453  -31.8744</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  141.7078  497.8501   60.2486 -156.7319   87.2906  -62.5703</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -160.2750  949.7077    6.3111  -22.9734 -101.2634   18.9416</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  -70.6819  863.6263   -2.0631  117.5866   40.5702   88.0529</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -163.3710  879.2684  -61.7499  -37.9675    0.0507  -22.3736</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -109.6284  498.0274  -30.4581   40.8510  -67.6815  -92.9724</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   79.2597  674.5477   31.3109  114.7107   17.1878  -13.4770</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   79.8312  898.0421   72.2572  139.0446  -90.6746  -47.9557</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  136.0077  946.8013   33.0054  155.2002   41.0799  -23.6672</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   29.6759  734.7714 -135.5329 -111.3175   23.9005   80.0073</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> -154.5536  365.4212   21.9464  -86.9104 -106.5657  -23.1291</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  152.1880  723.0805  -34.7579  143.2316 -106.4777  -26.3578</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"7\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">  108.1340  257.6412  -34.9232   33.6103  -83.3998  -33.4923</span></p></td></tr></table></body></html>", None))
        self.pushButton_3.setText(_translate("Dialog", "清除", None))
        self.label_3.setText(_translate("Dialog", "3.输入绝对误差", None))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    4.5745    5.9860    5.8098</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    0.5804    4.9337    4.6659</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    4.5573   -0.6489    9.4117</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    3.2142    1.0945    7.5895</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    4.9774    2.6425    0.4990</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -0.9895   -2.5060    6.2919</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -2.2421   -7.1856    2.6111</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    1.3035    4.6978    4.5720</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    4.6064    2.0101    8.9205</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -1.8633    0.4926    9.5929</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    0.2856   11.1200    4.1104</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -2.0487    8.5369    0.7637</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    7.5687    2.0139    4.3702</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -3.3806    5.0743    4.3040</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -1.1944    0.7500    2.6552</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    1.2020   -1.8746    3.4127</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    0.2962   -5.3818    6.5236</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    0.8928   -1.5225    4.0601</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    5.2226    3.6826    7.8113</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    8.6058    0.0412    7.9283</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    7.2137    3.9697    3.0570</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    0.2075   -3.6684    5.1075</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    2.4988    2.1671    3.3021</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    1.8192    5.1686    6.2141</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    2.5810    1.7570    7.5222</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    4.4382   -4.8826    4.9296</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    2.0568    4.7042    5.1980</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -1.2903   -1.8191    2.4183</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -2.4647    3.0144    6.3169</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    1.3666   -5.8373    4.4309</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -6.4000    1.2079    0.4317</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    5.9008    4.5222    3.5989</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -4.4057   -4.4233    3.8542</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    3.0806    1.0406    7.2174</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -4.5321    0.0440    0.5328</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -4.8693    4.8046   -0.4544</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    5.6614    7.0295    6.8795</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -2.3007    3.4135   -1.6990</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -5.4059   -2.9169    6.0164</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    1.1619   -2.5182   -0.4808</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    4.1267    0.0295    4.2583</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -4.0362   -2.0918    4.5425</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    7.1468   -5.7856    0.1441</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -2.5031    0.4762    4.3288</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    1.5152    0.1994   -1.0055</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -0.0196    1.5421    5.4045</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    5.7244    4.2475    8.4541</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    3.6624   -6.1269    0.1640</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -4.2434   -1.5037   -1.8195</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">   -8.9371    2.6175   -1.5485</span></p></td></tr></table></body></html>", None))
        self.pushButton_4.setText(_translate("Dialog", "清除", None))
        self.label_17.setText(_translate("Dialog", "4.計算DH誤差", None))
        self.pushButton.setText(_translate("Dialog", "確認參數", None))
        self.pushButton_2.setText(_translate("Dialog", "計算", None))
        self.label_18.setText(_translate("Dialog", "     Da1\n"
" Dalpha1\n"
" Dtheta1\n"
"     Dd1\n"
"     Da2\n"
" Dalpha2\n"
" Dtheta2\n"
"     Dd2\n"
"     Da3\n"
" Dalpha3\n"
" Dtheta3\n"
"     Dd3\n"
"     Da4\n"
" Dalpha4\n"
" Dtheta4\n"
"     Dd4\n"
"     Da5\n"
" Dalpha5\n"
" Dtheta5\n"
"     Dd5\n"
"     Da6\n"
" Dalpha6\n"
" Dtheta6\n"
"     Dd6\n"
"", None))


    def activeDHparameter(self):
        a=[1,365 ,235 ,300 ,0,0]
        alpha=[0, 0 ,0 , np.pi/2 ,np.pi/2,0]
        theta=[0, 0, 0, 0, 0,0]    
        d=[500,0, -143.97, 0,0,100]
        a[0]=self.a1.text()
        a[1]=self.a2.text()
        a[2]=self.a3.text()
        a[3]=self.a4.text()
        a[4]=self.a5.text()
        a[5]=self.a6.text()
        d[0]=self.d1.text()
        d[2]=self.d3.text()
        d[3]=self.d4.text()
        d[4]=self.d5.text()
        d[5]=self.d6.text()
        self.a=[float(i) for i in a]
        self.alpha=[float(i) for i in alpha]
        self.theta=[float(i) for i in theta]
        self.d=[float(i) for i in d]
#        self.time1=time.time()
        #print(self.aa)
        tempq=np.array(self.textEdit.toPlainText().split(), dtype=float)
        self.n=int((np.size(tempq))/6)
        self.q=tempq.reshape(self.n, 6)
        temperr=np.array(self.textEdit_2.toPlainText().split(), dtype=float)
        self.err=temperr.reshape(self.n, 3)
#        print(self.q)
#        print(self.err)
#        

#        print((a, alpha, theta, d)[0])
    def calculate(self):
        self.DDD=np.dot(np.linalg.pinv(self.j('jj')),self.j('ee'))
#        a=np.zeros(self.n)
#        for k in range(len(self.DDD)):
#            a[i]=round(self.DDD[i])
        a=[]
        for i in range(24):
            a.append(('%9.6f'%self.DDD[i][0]))
#        self.textEdit_3.setText(a[0:24])
        b=a
        for i in range(24):
            b[i]=a[i]+'\n'
        b=''.join(b)
        self.textEdit_3.setText(b)

    def trot(self, m,n):
    
        if m=='x':
            return np.mat([[1,0,0,0],
                          [0,cos(n),-sin(n),0],
                          [0,sin(n),cos(n),0],
                          [0,0,0,1]],dtype=float)
        elif m=='y':
            return np.mat([[cos(n),0,sin(n),0],
                        [0,1,0,0],
                        [-sin(n),0,cos(n),0],
                        [0,0,0,1]])
        elif m=='z':
            return np.mat([[cos(n),-sin(n),0,0],
                        [sin(n),cos(n),0,0],
                        [0,0,1,0],
                        [0,0,0,1]])    
    def transl(self, m,n):
    
        if m=='x':
            return np.mat([[1,0,0,n],
                    [0,1,0,0],
                    [0,0,1,0],
                    [0,0,0,1]])
    
        if m=='y':
            return np.mat([[1,0,0,0],
                    [0,1,0,n],
                    [0,0,1,0],
                    [0,0,0,1]])
        if m=='z':
            return np.mat([[1,0,0,0],
                    [0,1,0,0],
                    [0,0,1,n],
                    [0,0,0,1]])
    #DH参数待定
    

    def A(self, p):
        a=self.a
        alpha=self.alpha
        theta=self.theta
        d=self.d
        theta[0]=p[0]
        d[1]=p[1]
        theta[2]=p[2]
        theta[3]=p[3]
        theta[4]=p[4]
        theta[5]=p[5]
        T={}
        for i in range(6):
            T[i]=(self.trot('z',theta[i])*self.transl('z',d[i])*self.transl('x',a[i])*self.trot('x',alpha[i]))
        return T
    def M(self, n,p):
        a=self.A(p)
        if n==0:
            return a[0]*a[1]*a[2]*a[3]*a[4]*a[5]
        elif n==1:
            return a[1]*a[2]*a[3]*a[4]*a[5]
        elif n==2:
            return a[2]*a[3]*a[4]*a[5]
        elif n==3:
            return a[3]*a[4]*a[5]
        elif n==4:
            return a[4]*a[5]
        elif n==5:
            return a[5]
        elif n==6:
            return np.mat(np.eye(4,4))
        
    def JJ(self, p):
        JJ={}
        JJ[6]=np.eye(6,6)
        for i in range(6):
            pp=self.M(i,p)[0:3,3].T
            nn=self.M(i,p)[0:3,0].T
            oo=self.M(i,p)[0:3,1].T
            aa=self.M(i,p)[0:3,2].T
            JJ[i]=np.mat(np.zeros((6,6)))
            JJ[i][:3,:3]=self.M(i,p)[0:3,0:3].T
            JJ[i][3:,3:]=self.M(i,p)[0:3,0:3].T
            JJ[i][0,3:]=np.cross(pp,nn)
            JJ[i][1,3:]=np.cross(pp,oo)
            JJ[i][2,3:]=np.cross(pp,aa)
        return JJ
 #       print(time.time()-self.time1)
    def GG(self):
        a=self.a
        alpha=self.alpha
        G={}
        for i in range(6):
            G[i]=np.mat([[1 ,0 ,0 ,0],
                  [0,0 ,a[i]*cos(alpha[i]) ,sin(alpha[i])],
                  [0 ,0, -a[i]*sin(alpha[i]) ,cos(alpha[i])],
                  [0 ,1, 0 ,0],
                  [0, 0, sin(alpha[i]), 0],
                  [0 ,0,cos(alpha[i]),0]])
    
        return G
    def JG(self, p):
        J=self.JJ(p)
        G=self.GG()
        return np.hstack((J[1]*G[0],J[2]*G[1],J[3]*G[2],J[4]*G[3],J[5]*G[4],J[6]*G[5]))
    
    def j(self, jj_e):

        #位置误差识别矩阵3nx24,与末端误差转换
        jgg={}
        ee={}
        for i in range(self.n):
            p=self.q[i]
            pp=[radians(p[0]),p[1],radians(p[2]),radians(p[3]),radians(p[4]),radians(p[5])]
            jgg[i]=(self.JG(pp)[0:3,:])
            error_basecoordinate=np.array([[0,0,0,0]],dtype=float).T
            error_basecoordinate[0:3]=np.array([self.err[i]]).T
            transfer=np.array(self.M(0,pp),dtype=float)
            error_endcoordinate=np.linalg.solve(transfer,error_basecoordinate)
            ee[i]=(error_endcoordinate[0:3])
        jggg=np.array(np.vstack((jgg[i]) for i in jgg) ,dtype=float)
        e=np.array(np.vstack((ee[i]) for i in ee),dtype=float)
        if jj_e=='jj':
            return jggg
        elif jj_e=='ee':
            return e
#        print(time()-self.time1)


        
     #   print(time.time()-self.time1)



if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



