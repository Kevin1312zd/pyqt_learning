import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QAbstractItemView,QListView,QListWidgetItem
from listwdgt import Ui_MainWindow
from collections import OrderedDict

class listWdgt(QMainWindow,Ui_MainWindow): #listWidget实现票房显示
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)    #设置列表中可以多选
        self.ui.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)   #选中整行

        self.ui.listWidget.setViewMode(QListView.ListMode)                       #设置以列表的形式显示数据
        self.ui.listWidget.setWordWrap(True)

        dict = OrderedDict({'第一名':'战狼2','第二名':'哪吒','第三名':'流浪地球','第四名':'复仇者联盟5','第五名':'红海行动','第六名':'唐人街探案2'})

        for key,value in dict.items():                       #遍历有序字典，并分别获取到键和值
            self.item=QListWidgetItem(self.ui.listWidget)    #创建列表项
            self.item.setText(key+' : '+value)                 #设置项文本
            self.item.setToolTip(value)                      #设置提示文字

        self.ui.listWidget.itemClicked.connect(self.gettext)

    def gettext(self,Item):
        if Item.isSelected():
            QMessageBox.information(self, "提示", "您选择的是："+Item.text(), QMessageBox.Ok)

if __name__=='__main__':
    app = QApplication(sys.argv)
    listw = listWdgt()
    listw.show()
    sys.exit(app.exec_())