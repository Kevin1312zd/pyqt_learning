import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox,QMessageBox
from checkbox import Ui_MainWindow

class checkBox(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.getvalue)

    def getvalue(self):
        oper='' #记录用户权限
        if self.ui.checkBox.isChecked():
            oper+=self.ui.checkBox.text()+'\n'
        if self.ui.checkBox_2.isChecked():
            oper+=self.ui.checkBox_2.text()+'\n'
        if self.ui.checkBox_3.isChecked():
            oper += self.ui.checkBox_3.text()+'\n'
        if self.ui.checkBox_4.isChecked():
            oper+=self.ui.checkBox_4.text()+'\n'
        if self.ui.checkBox_5.isChecked():
            oper+=self.ui.checkBox_5.text()+'\n'
        QMessageBox.information(self,"提示","您选择的管理权限为:\n"+oper,QMessageBox.Ok)


if __name__=='__main__':
    app=QApplication(sys.argv)
    checkb=checkBox()
    checkb.show()
    sys.exit(app.exec_())