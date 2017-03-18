

from PyQt4 import QtCore, QtGui
import  Ui_ys01,Ui_P1P5
#QtGui.QApplication.addLibraryPath("./plugins")
#import os
#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\anaconda3\Lib\site-packages\PyQt4\plugins'
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
        Dialog.resize(801, 510)
        Dialog.setSizeGripEnabled(True)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 120, 161, 101))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 120, 151, 101))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.DH)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.P1P5)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "YS01-PT-Rel-version1.0", None))
        self.pushButton_2.setText(_translate("Dialog", "计算P1-P5", None))
        self.pushButton.setText(_translate("Dialog", "计算DH误差", None))

    def DH(self):
        DH=QtGui.QDialog()
        DHui=Ui_ys01.Ui_Dialog()
        DHui.setupUi(DH)
        DH.exec_()

    def P1P5(self):
        DH=QtGui.QDialog()
        DHui=Ui_P1P5.Ui_Dialog()
        DHui.setupUi(DH)
        DH.exec_()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

