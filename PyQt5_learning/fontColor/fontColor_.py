import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFontDialog,QColorDialog
from fontColor import Ui_MainWindow

class fontclor(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.setfont)
        self.ui.pushButton_2.clicked.connect(self.setcolor)

    def setfont(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.ui.textEdit.setFont(font)
    def setcolor(self):
        color=QColorDialog.getColor()
        if color.isValid():
            self.ui.textEdit.setTextColor(color)



if __name__=='__main__':
    app =QApplication(sys.argv)
    fontc = fontclor()
    fontc.show()
    sys.exit(app.exec_())