import sys
from PyQt5.QtWidgets import *
from tablewidget import Ui_MainWindow

import pymysql

class tablewidgt(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.setupUi(self)

        #打开数据库连接
        db=pymysql.connect("192.168.254.183","root", "root123...", "movedb", 13306,'utf8')
        cursor=db.cursor()
        cursor.execute("SELECT * from `索引表`")
        result=cursor.fetchall()
        row=cursor.rowcount
        vol=len(result[0])
        cursor.close()
        db.close()
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(vol)
        for i in range(row):
            for j in range(vol):
                data=QTABLE



if __name__ == '__main__':
    app=QApplication(sys.argv)
    tablew=tablewidgt()
    tablew.show()
    sys.exit(app.exec_())