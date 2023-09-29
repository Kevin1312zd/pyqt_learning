import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QLineEdit
from Pushbtn import  Ui_MainWindow


class pushBtn(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_2.setValidator(QtGui.QIntValidator(100000000,99999999))   #设置密码为8位数字
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)                         #设置文本框为密码

        #self.ui.radioButton.setAutoExclusive(True)
        #self.ui.radioButton_2.setAutoExclusive(True)


        self.ui.radioButton.setChecked(True) #设置管理员按钮默认选中
        self.ui.radioButton.toggled.connect(self.select)
        #self.ui.radioButton_2.toggled.connect(self.select)  #使用这行代码会导致消息对话框弹出两次，因为select被执行了两次


        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.close)



    def login(self):
        QMessageBox.information(self,"登录信息","用户名："+self.ui.lineEdit.text()+"密码："+self.ui.lineEdit_2.text(),QMessageBox.Ok)

    def select(self):
        if self.ui.radioButton.isChecked():#判断是否为管理员登录
            QMessageBox.information(self,"提示","您选中的是管理员登录",QMessageBox.Ok)
        elif self.ui.radioButton_2.isChecked():#判断是否为普通用户登录
            QMessageBox.information(self,"提示","您选中的是普通用户登录",QMessageBox.Ok)



if __name__=='__main__':
    app=QApplication(sys.argv)
    pushbtn=pushBtn()
    pushbtn.show()
    sys.exit(app.exec_())
