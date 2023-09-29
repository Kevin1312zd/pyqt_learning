import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
from dial import Ui_MainWindow

class dial_(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.setupUi(self)

        self.dial.setMaximum(72)              #获取最大值
        self.dial.setMinimum(8)               #获取最小值
        self.dial.setNotchesVisible(True)     #设置显示刻度

        self.dial.valueChanged.connect(self.setfontsize)    #添加信号

    def setfontsize(self):
        value = self.dial.value()
        self.label.setFont(QtGui.QFont("楷体",value))



if __name__ == '__main__':
    app=QApplication(sys.argv)
    dial=dial_()
    dial.show()
    sys.exit(app.exec_())



# class dial_(QMainWindow,Ui_MainWindow):
#     def __init__(self,parent=None):
#         super(QMainWindow,self).__init__(parent)
#         self.ui=Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         self.ui.dial.setMaximum(72)           #设置最小值
#         self.ui.dial.setMinimum(8)            #设置最大值
#         self.ui.dial.setNotchesVisible(True)  #设置显示刻度
#
#         self.ui.dial.valueChanged.connect(self.setfontsize)
#
#     def setfontsize(self):
#         value=self.ui.dial.value()
#         self.ui.label.setFont(QtGui.QFont("楷体",value))
#
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     d=dial_()
#     d.show()
#     sys.exit(app.exec_())
