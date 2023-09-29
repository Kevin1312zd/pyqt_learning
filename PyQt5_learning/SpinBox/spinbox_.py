import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication,QSpinBox,QLabel
from spinbox import Ui_MainWindow

class SpinBox(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.spinBox.setMinimum(0)    #设置最小值
        self.ui.spinBox.setMaximum(200)  #设置最大值
        #self.ui.spinBox.setRange(0,200)  #设置范围
        self.ui.spinBox.setSingleStep(2)    #设置步长值

        self.ui.spinBox.valueChanged.connect(self.getValue) #更改spinBox中数值时发射信号

    def getValue(self):
        self.ui.label_2.setText(str(self.ui.spinBox.value())) #获取spinBox中的数值，并在label中显示

if __name__=='__main__':
    app = QApplication(sys.argv)
    spinbox = SpinBox()
    spinbox.show()
    sys.exit(app.exec_())
