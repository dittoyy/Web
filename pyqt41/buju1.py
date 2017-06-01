#coding=gbk
import sys
from PyQt4 import QtCore, QtGui
class Window( QtGui.QWidget ):
     def __init__( self ):
         super ( Window, self ).__init__()
         self .setWindowTitle( "hello" )
         self .resize( 500 , 500 )

         hBoxLayout1 = QtGui.QHBoxLayout()

         label1 = QtGui.QLabel( "Label1" )
         label2 = QtGui.QLabel( "Label2" )
         label3 = QtGui.QLabel( "Label3" )
         label4 = QtGui.QLabel( "Label4" )
         label5 = QtGui.QLabel( "Label5" )
         #---------添加表格布局
         gridLayout = QtGui.QGridLayout()

         gridLayout.addWidget( label1 , 0 , 0 )
         gridLayout.addWidget( label2 , 0 , 1 )
         gridLayout.addWidget( label3 , 0 , 2 )
         gridLayout.addWidget( label4 , 1 , 0 )
         gridLayout.addWidget( label5 , 1 , 1 )

         self .setLayout( gridLayout )
#-------添加水平布局
#        hBoxLayout1.addWidget( label1 )
#        hBoxLayout1.addWidget( label2 )
#        hBoxLayout1.addWidget( label3 )
#        hBoxLayout1.addWidget( label4 )
#        hBoxLayout1.addWidget( label5 )
#
#        self.setLayout( hBoxLayout1 )

#---------添加垂直布局
#        vBoxLayout = QtGui.QVBoxLayout()
#        vBoxLayout.addWidget( label1 )
#        vBoxLayout.addWidget( label2 )
#        vBoxLayout.addWidget( label3 )
#        vBoxLayout.addWidget( label4 )
#        vBoxLayout.addWidget( label5 )
#
#        self.setLayout( vBoxLayout )
#


app = QtGui.QApplication( sys.argv )
demo = Window()
demo.show()
app.exec_()