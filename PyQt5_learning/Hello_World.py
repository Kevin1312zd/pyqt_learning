import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=QWidget()
    layout=QHBoxLayout()
    btn=QPushButton("Hello World!")
    layout.addWidget(btn)
    w.setLayout(layout)
    w.show()
    sys.exit(app.exec_())


