import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QCalendarWidget
from calendar import Ui_MainWindow

class calendarWdgt(QMainWindow,Ui_MainWindow):
    def __innit__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.calendarWidget = QCalendarWidget(self.ui.centralwidget)
        self.ui.calendarWidget.selectedDate(QtCore.QDate(20223,9,20))   #设置默认选中日期
        self.ui.calendarWidget.setMinimumDate(QtCore.QDate(1752,9,14))  #设置最小日期
        self.ui.calendarWidget.setMaximumDate(QtCore.QDate(9999,12,20)) #设置最大日期
        self.ui.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)      #设置每周的第一天为周一
        self.ui.calendarWidget.setGridVisible(True)                     #设置网格线可见

        self.ui.calendarWidget.setSelectionMode(QCalendarWidget.SingleSelection) #设置可选中单个日期
        self.ui.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)#设置水平表头为简短形式
        self.ui.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers) #设置垂直表头为周数

        self.ui.calendarWidget.setNavigationBarVisible(True) #设置显示导航栏
        self.ui.calendarWidget.setDateEditEnabled(True) #设置日期可以编辑

        self.ui.calendarWidget.selectionChanged.connect(self.getdata) #选中日期发生变化时发射信号


    def getdata(self):

        date=QtCore.QDate(self.ui.calendarWidget.selectedDate())#获取当前选中日期的QDate对象
        year=date.year()
        month=date.month()
        day=date.day()
        QMessageBox.information(self,"提示",str(year)+"-"+str(month)+"-"+str(day),QMessageBox.Ok)



if __name__=='__main__':

    app = QApplication(sys.argv)
    calendarw = calendarWdgt()
    calendarw.show()
    sys.exit(app.exec_())