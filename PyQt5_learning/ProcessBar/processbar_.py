import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow
from processbar import Ui_MainWindow

class processBar(QMainWindow,Ui_MainWindow):  #四个进度条实现跑马灯效果
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer=QtCore.QBasicTimer()  #创建计时器对象
        self.ui.pushButton.clicked.connect(self.running)
    def running(self):#控制进度条的滚动效果
        if self.timer.isActive(): #判断计时器是否开启
            self.timer.stop()     #停止计时器
            self.ui.pushButton.setText("开始")  #设置按钮的文本

            #设置四个进度条的最大值为100
            self.ui.progressBar.setMinimum(100)
            self.ui.progressBar_2.setMinimum(100)
            self.ui.progressBar_3.setMinimum(100)
            self.ui.progressBar_4.setMinimum(100)
        else:
            self.timer.start(100,self)
            self.ui.pushButton.setText("停止")

            #将四个进度条的最大值和最大值都设置成0，以便实现循环滚动显示效果
            self.ui.progressBar.setInvertedAppearance(True)  # 设置进度条反向显示
            self.ui.progressBar.setMinimum(0)
            self.ui.progressBar.setMaximum(0)
            self.ui.progressBar_2.setInvertedAppearance(True) #设置进度条反向显示
            self.ui.progressBar_2.setMinimum(0)
            self.ui.progressBar_2.setMaximum(0)
            self.ui.progressBar_3.setMinimum(0)
            self.ui.progressBar_3.setMaximum(0)
            self.ui.progressBar_4.setMinimum(0)
            self.ui.progressBar_4.setMaximum(0)

if __name__=='__main__':
    app=QApplication(sys.argv)
    processb=processBar()
    processb.show()
    sys.exit(app.exec_())