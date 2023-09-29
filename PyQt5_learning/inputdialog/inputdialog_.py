import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QInputDialog,QLineEdit
from inputdialog import Ui_MainWindow

class inputdia(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit.returnPressed.connect(self.getname)        #为’姓名‘文本框的按下回车信号绑定槽函数，获取用户输入的姓名
        self.ui.lineEdit_2.returnPressed.connect(self.getage)       #为‘年龄’文本框的按下回车信号绑定槽函数，获取用户输入的年龄
        self.ui.lineEdit_3.returnPressed.connect(self.getgrade)     #为‘班级’文本框的按下回车信号绑定槽函数，获取用户输入的班级
        self.ui.lineEdit_4.returnPressed.connect(self.getscore)     #为‘分数’文本框的按下回车信号绑定槽函数，获取用户输入的分数

    def getname(self):
        name,ok=QInputDialog.getText(self,"姓名","请输入姓名：",QLineEdit.Normal,"张栋") #name表示文本编辑框内的输入的字符串内容，ok表示是否正常返回
        if ok: #判断是否单击了”OK“按钮
            self.ui.lineEdit.setText(name) #将输入内容显示在文本框中
    def getage(self):
        age,ok=QInputDialog.getInt(self,"年龄","请输入年龄：",25,1,150,1)
        if ok:
            self.ui.lineEdit_2.setText(str(age))
    def getgrade(self):
        grade, ok = QInputDialog.getItem(self, "分数", "请输入分数：",("研一","研二","研三"),0,False)
        if ok:
            self.ui.lineEdit_3.setText(str(grade))
    def getscore(self):
        score, ok = QInputDialog.getDouble(self, "分数", "请输入分数：", 95, 0, 100, 2)
        if ok:
            self.ui.lineEdit_4.setText(str(score))

if __name__=='__main__':
    app = QApplication(sys.argv)
    inputd = inputdia()
    inputd.show()
    sys.exit(app.exec_())