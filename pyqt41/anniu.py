#coding=utf-8
#按钮操作

import sys
from PyQt4 import QtGui, QtCore
class Window( QtGui.QWidget ):
     def __init__( self ):
         super ( Window, self ).__init__()
         self .setWindowTitle( "hello" )
         self .resize( 500 , 500 )
         gridlayout = QtGui.QGridLayout()

         button1 = QtGui.QPushButton( "button1" )
         gridlayout.addWidget( button1, 0 , 0 , 1 , 3 )

         button2 = QtGui.QPushButton( "button2" )
         button2.setFlat( True )
         gridlayout.addWidget( button2, 1 , 1 , 1 , 3 )
         self .setLayout( gridlayout )
app = QtGui.QApplication( sys.argv )
demo = Window()
demo.show()
app.exec_()