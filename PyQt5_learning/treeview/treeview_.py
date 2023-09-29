import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QAbstractItemView,QDirModel
from treeview import Ui_MainWindow

class Treeview(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.treeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)    #设置垂直滚动条为按需显示
        self.ui.treeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)  #设置水平滚动条为按需显示
        self.ui.treeView.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed) #设置在双击或者按下回车键时，使树节点可编辑
        self.ui.treeView.setSelectionBehavior(QAbstractItemView.SelectRows)    #设置选中节点时为整行选定
        self.ui.treeView.setAutoExpandDelay(-1)         #设置自动展开时延为-1，代表自动展开不可用
        self.ui.treeView.setItemsExpandable(True)       #设置是否可以展开项
        self.ui.treeView.setSortingEnabled(True)        #设置单击头部可排序
        self.ui.treeView.setWordWrap(True)              #设置自动换行
        self.ui.treeView.setHeaderHidden(False)         #设置不隐藏头部
        self.ui.treeView.setExpandsOnDoubleClick(True)  #设置双击可以展开节点
        self.ui.treeView.header().setVisible(True)      #设置显示头部

        model=QDirModel()                               #创建存储文件系统的模型
        self.ui.treeView.setModel(model)                #为树控件设置数据模型




if __name__=='__main__':
    app=QApplication(sys.argv)
    treev=Treeview()
    treev.show()
    sys.exit(app.exec_())