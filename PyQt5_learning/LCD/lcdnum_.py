import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QLCDNumber,QLineEdit
from lcdnum import Ui_MainWindow

class LcdNumber(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lcdNumber.setDigitCount(7)           #设置最大显示7位数字
        self.ui.lcdNumber.setMode(QLCDNumber.Dec)    #设置默认以十进制显示数字
        self.ui.lcdNumber.setSegmentStyle(QLCDNumber.Flat)  #设置数字显示屏的显示样式

        self.ui.lineEdit.editingFinished.connect(self.setValue) #将信号连接槽函数

    def setValue(self):
        self.ui.lcdNumber.setProperty("value" , self.ui.lineEdit.text()) #使用setProperty方法为lcdNumber控件设置设置要显示的数字为LineEdit文本框中输入的数字

if __name__=='__main__':
    app=QApplication(sys.argv)
    lcdnum=LcdNumber()
    lcdnum.show()
    sys.exit(app.exec_())