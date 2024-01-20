from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from calcUI import *

class Nithya(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.clear.clicked.connect(self.c)
        self.ui.pm.clicked.connect(self.pm)
        self.ui.percent.clicked.connect(self.per)
        self.ui.div.clicked.connect(self.d)
        self.ui.one.clicked.connect(self.one)
        self.ui.two.clicked.connect(self.two)
        self.ui.three.clicked.connect(self.thr)
        self.ui.four.clicked.connect(self.four)
        self.ui.five.clicked.connect(self.five)
        self.ui.six.clicked.connect(self.six)
        self.ui.seven.clicked.connect(self.sev)
        self.ui.eight.clicked.connect(self.ei)
        self.ui.nine.clicked.connect(self.nine)
        self.ui.zero.clicked.connect(self.zero)
        self.ui.point.clicked.connect(self.point)
        self.ui.mul.clicked.connect(self.mul)
        self.ui.sub.clicked.connect(self.sub)
        self.ui.add.clicked.connect(self.add)
        self.ui.equal.clicked.connect(self.sol)
    def pm(self):
        if self.ui.type.text()[0] != '-':
            self.ui.type.setText('-{}'.format(self.ui.type.text()))
        else:
            self.ui.type.setText('{}'.format(self.ui.type.text()[1:]))
    def per(self):
        self.ui.type.setText('{} % '.format(self.ui.type.text()))
    def c(self):
        self.ui.type.setText(self.ui.type.clear())
    def one(self):
        self.ui.type.setText('{}1'.format(self.ui.type.text()))
    def two(self):
        self.ui.type.setText('{}2'.format(self.ui.type.text()))
    def thr(self):
        self.ui.type.setText('{}3'.format(self.ui.type.text()))
    def four(self):
        self.ui.type.setText('{}4'.format(self.ui.type.text()))
    def five(self):
        self.ui.type.setText('{}5'.format(self.ui.type.text()))
    def six(self):
        self.ui.type.setText('{}6'.format(self.ui.type.text()))
    def sev(self):
        self.ui.type.setText('{}7'.format(self.ui.type.text()))
    def ei(self):
        self.ui.type.setText('{}8'.format(self.ui.type.text()))
    def nine(self):
        self.ui.type.setText('{}9'.format(self.ui.type.text()))
    def zero(self):
        self.ui.type.setText('{}0'.format(self.ui.type.text()))
    def add(self):
        self.ui.type.setText('{} + '.format(self.ui.type.text()))
    def sub(self):
        self.ui.type.setText('{} - '.format(self.ui.type.text()))
    def mul(self):
        self.ui.type.setText('{} x '.format(self.ui.type.text()))
    def d(self):
        self.ui.type.setText('{} / '.format(self.ui.type.text()))
    def point(self):
        self.ui.type.setText('{}.'.format(self.ui.type.text()))
    def sol(self):
        s=self.ui.type.text()
        if '%' in s:
            self.ui.type.setText('{}'.format(eval(self.ui.type.text().replace('x','*').replace('%','*'))/100))
        else:
            self.ui.type.setText('{}'.format(eval(self.ui.type.text().replace('x','*'))))
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Nithya()
    w.show()
    sys.exit(app.exec_())
