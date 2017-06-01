# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first1.ui'
#
# Created: Wed May 31 12:13:09 2017
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.price_box = QtGui.QTextEdit(self.centralwidget)
        self.price_box.setGeometry(QtCore.QRect(150, 90, 104, 71))
        self.price_box.setObjectName(_fromUtf8("price_box"))
        self.tax_rate = QtGui.QSpinBox(self.centralwidget)
        self.tax_rate.setGeometry(QtCore.QRect(180, 250, 42, 22))
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName(_fromUtf8("tax_rate"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 110, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 260, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.calc_tax_button = QtGui.QPushButton(self.centralwidget)
        self.calc_tax_button.setGeometry(QtCore.QRect(124, 350, 121, 21))
        self.calc_tax_button.setObjectName(_fromUtf8("calc_tax_button"))
        self.results_window = QtGui.QTextEdit(self.centralwidget)
        self.results_window.setGeometry(QtCore.QRect(140, 450, 104, 71))
        self.results_window.setObjectName(_fromUtf8("results_window"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Tax Price", None, QtGui.QApplication.UnicodeUTF8))
        self.calc_tax_button.setText(QtGui.QApplication.translate("MainWindow", "calc_tax_button", None, QtGui.QApplication.UnicodeUTF8))

class MainWindow(QtGui.QMainWindow,Ui_mainWindow):
    """def __init__(self,parent=None):
        super(Ui_mainWindow2,self).__init__(parent)
        self.setupUi(self)
    """
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
import sys
app=QtGui.Application(sys.argv)
mainwindow=MainWindow()
mainwindow.show()
sys.exit(app.exec_())
