import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeWidgetItem,QMessageBox
from treewidget import Ui_MainWindow

class treewdgt(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.treeWidget.setColumnCount(2)                     #设置树结构中的列数
        self.ui.treeWidget.setHeaderLabels((['姓名','职务']))      #设置列标题名
        root = QTreeWidgetItem(self.ui.treeWidget)               #创建节点
        root.setText(0,'组织结构')                                 #设置顶级节点文本

        #定义字典，存储树结构中显示的数据
        dict = {'任正非':'华为董事长','马云':'阿里巴巴创始人','马化腾':'腾讯CEO','李彦宏':'百度CEO','董明珠':'格力董事长'}

        for key,value in dict.items():                 #遍历字典
            child = QTreeWidgetItem(root)              #创建子节点
            child_child = QTreeWidgetItem(child)       #创建下级子节点
            child.setText(0,key)                       #设置第一列的值
            child.setText(1,value)                     #设置第二列的值
            child.setCheckState(0,QtCore.Qt.Unchecked) #为节点设置复选框，并且选中。Qt.Unchecked()为未选中
            child_child.setText(0,key)
            child_child.setText(1,value)

        self.ui.treeWidget.addTopLevelItem(root)       #将创建的树节点添加到树控件中
        self.ui.treeWidget.expandAll()                 #展开所有树节点

        self.ui.treeWidget.setAlternatingRowColors(True) #设置隔行变色

        self.ui.treeWidget.clicked.connect(self.gettreetext)  #为树控件绑定单击信号

    def gettreetext(self):
        item = self.ui.treeWidget.currentItem()   #获取当前选中项
        #弹出提示框，显示选中的文本
        QMessageBox.information(self,"提示","您选择的是：%s -- %s"%(item.text(0),item.text(1)),QMessageBox.Ok)



if __name__=='__main__':
    app = QApplication(sys.argv)
    treew = treewdgt()
    treew.show()
    sys.exit(app.exec_())
