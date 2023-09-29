import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
from treeview import Ui_MainWindow
import random

class Treeview_1(QMainWindow,Ui_MainWindow):   #使用QStandardItemModel创建自定义数据,并在treeView中显示
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        model=QtGui.QStandardItemModel() #创建数据模型
        model.setHorizontalHeaderLabels(['年级','班级','姓名','分数'])

        name=['张三','李四','向明','小红','小兰','丽丽','王刚','小林','安白']
        score=[65, 89, 45, 68, 90, 100, 99, 76, 78]

        for i in range(0,6):
            #一级节点：年级，只设第1列的数据
            grade = QtGui.QStandardItem(("%s年级")%(i+1))
            model.appendRow(grade)
            for j in range(0,4):
                #二级节点：班级、姓名、分数
                itemClass=QtGui.QStandardItem(("%s班级")%(j+1))
                itemName=QtGui.QStandardItem(name[random.randrange(9)])
                itemScore=QtGui.QStandardItem(str(score[random.randrange(9)]))
                #将二级节点添加到一级节点上
                grade.appendRow([QtGui.QStandardItem(""),itemClass,itemName,itemScore])

        self.ui.treeView.setModel(model)



if __name__=='__main__':
    app=QApplication(sys.argv)
    treev=Treeview_1()
    treev.show()
    sys.exit(app.exec_())
