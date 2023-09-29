import sys
from PyQt5.QtGui import QImage,QPixmap #QImage和QPixmap 用于处理图像
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog,QGraphicsPixmapItem, QGraphicsScene #QGraphicsPixmapItem用于在图形视图中显示图片项；QGraphicsScene用于管理图片项的场景
from filedialog import Ui_MainWindow

class filedia(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        # 使用graphicsView显示图片
        self.scene = QGraphicsScene()  # 创建画布
        self.ui.graphicsView.setScene(self.scene)  # 把画布添加到窗口
        self.ui.graphicsView.show()

        self.ui.pushButton.clicked.connect(self.bindlist)               #选择文件并进行显示

        self.ui.listWidget.itemClicked.connect(self.clickopenscene)     #在点击listWidget中的项时，会显示相对应的图片

    def bindlist(self):
        dir = QFileDialog()                           #创建文件对话框
        dir.setFileMode(QFileDialog.ExistingFile)     #设置可以单选
        dir.setDirectory('C:\\')                      #设置初始路径为C盘
        dir.setNameFilter('图片文件(*.jpg *.png .*bmp  *.ico *.gif)')  #设置只显示图片文件
        if dir.exec_():   #判断是否选择了文件
            self.ui.listWidget.addItems(dir.selectedFiles()) #将选择的文件显示在列表中
            image_name = dir.selectedFiles()
            #print(image_name)
            for img in image_name:
                frame = QImage(img)                  #通过QImage创建了一个图像帧。
                pix = QPixmap.fromImage(frame)       #使用 QPixmap.fromImage创建了一个 QPixmap 对象，这是一个可显示在图形视图中的图像对象。
                item = QGraphicsPixmapItem(pix)      #创建了一个 QGraphicsPixmapItem 对象，并将 pix 图像附加到这个图像项上。
                scene = QGraphicsScene()             #创建了一个 QGraphicsScene 场景对象，用于管理图形项。
                scene.addItem(item)                  #将item添加到scene中。
                self.ui.graphicsView.setScene(scene) #在 graphicsView 中显示场景中的图形项。

    def clickopenscene(self,item):
        image_name=item.text()
        #print(image_name)
        frame = QImage(image_name)
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.ui.graphicsView.setScene(scene)

if __name__=='__main__':
    app=QApplication(sys.argv)
    filed=filedia()
    filed.show()
    sys.exit(app.exec_())