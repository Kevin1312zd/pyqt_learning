import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QSlider
from slider import Ui_MainWindow

class qslider(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #水平滑块
        self.ui.horizontalSlider.setMinimum(8)       #设置最小值为8
        self.ui.horizontalSlider.setMaximum(72)      #设置最大值为72
        self.ui.horizontalSlider.setSingleStep(1)    #设置通过鼠标拖动时的步长值
        self.ui.horizontalSlider.setPageStep(1)      #设置通过鼠标点击时的步长值
        self.ui.horizontalSlider.setProperty("value",8)    #设置默认值为8
        self.ui.horizontalSlider.setTickPosition(QSlider.TicksAbove)    #在水平滑块上面显示刻度
        self.ui.horizontalSlider.setTickInterval(3)  #设置水平滑块的刻度的间隔
        #垂直滑块
        self.ui.verticalSlider.setMinimum(8)    #设置最小值为8
        self.ui.verticalSlider.setMaximum(72)   #设置最大值为72
        self.ui.verticalSlider.setInvertedAppearance(True)  #设置刻度反向显示
        self.ui.verticalSlider.setTickPosition(QSlider.TicksRight)  #在滑块右侧显示刻度
        self.ui.verticalSlider.setTickInterval(3) #设置刻度的间隔

        self.ui.horizontalSlider.valueChanged.connect(self.setfontsize) #在水平滑块数值改变时发射信号

    def setfontsize(self):

        value=self.ui.horizontalSlider.value()   #获取水平滑块的数值
        self.ui.verticalSlider.setValue(value)   #将垂直滑块的数值设置为该数值
        self.ui.label.setFont(QtGui.QFont("楷体",value)) #通过该数值动态修改label的字体大小


if __name__=='__main__':
    app=QApplication(sys.argv)
    slid=qslider()
    slid.show()
    sys.exit(app.exec_())