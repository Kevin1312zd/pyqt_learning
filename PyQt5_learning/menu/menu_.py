import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QMessageBox,QLabel
from menu import Ui_MainWindow

class Menu(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNew.setShortcut("Ctrl+N")  #设置快捷键
        self.ui.actionOpen.setShortcut("Ctrl+O")
        self.ui.actionShutDown.setShortcut("Ctrl+S")

        self.ui.actionNew.triggered.connect(self.getmenuNew)  #在单击菜单项时发射信号
        self.ui.actionOpen.triggered.connect(self.getmenuOpen)
        self.ui.actionShutDown.triggered.connect(self.getmenuShut)

        self.ui.label=QLabel()
        self.ui.label.setText('敢想敢为，胆大心细')
        self.ui.statusbar.addPermanentWidget(self.ui.label)

        #在状态栏中显示日期时间
        timer=QtCore.QTimer(self)               #创建一个QTimer计时器对象
        timer.timeout.connect(self.showtime)    #发射timeout信号，与自定义槽函数关联
        timer.start()

    def showtime(self):
        datetime = QtCore.QDateTime.currentDateTime()  #获取当前日期时间
        text= datetime.toString("yyyy-MM-dd HH:mm:ss") #对日期时间进行格式化
        self.ui.statusbar.showMessage('当前日期时间：'+text,0) #在状态栏中显示时间日期


    def getmenuNew(self): #菜单栏槽函数
        QMessageBox.information(self,"提示","您选择的是： "+self.ui.actionNew.text(),QMessageBox.Ok)
    def getmenuOpen(self):
        QMessageBox.information(self,"提示","您选择的是： "+self.ui.actionOpen.text(),QMessageBox.Ok)
    def getmenuShut(self):
        reply = QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()


if __name__=='__main__':
    app=QApplication(sys.argv)
    menub=Menu()
    menub.show()
    sys.exit(app.exec_())