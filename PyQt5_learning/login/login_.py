import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
from login import Ui_Form

class MainWindow(QMainWindow,Ui_Form):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)                        #设置文本框为密码
        self.ui.lineEdit_2.setValidator(QtGui.QIntValidator(10000000,99999999))   #设置只能输入8位数字

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
