# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import sys

from PyQt4.QtWidgets import QApplication , QMainWindow

from qt1 import *

if __name__ == '__main__':
    '''
    主函数
    '''

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())