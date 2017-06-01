import sys
from PyQt4 import QtGui, QtCore
class Window( QtGui.QWidget ):
     def __init__( self ):
         super ( Window, self ).__init__()
         self .setWindowTitle( "hello" )
         self .resize( 500 , 500 )
         hboxlayout = QtGui.QHBoxLayout()

         self .radio1 = QtGui.QRadioButton( "radio1" )
         self .radio2 = QtGui.QRadioButton( "radio2" )
         self .radio3 = QtGui.QRadioButton( "radio3" )
         self .radio1.setChecked( True )

         hboxlayout.addWidget( self .radio1 )
         hboxlayout.addWidget( self .radio2 )
         hboxlayout.addWidget( self .radio3 )

         checkbox1 = QtGui.QCheckBox( "checkbox1" )
         checkbox2 = QtGui.QCheckBox( "checkbox2" )
         checkbox3 = QtGui.QCheckBox( "checkbox3" )
         checkbox1.setChecked( True )

         hboxlayout.addWidget( checkbox1 )
         hboxlayout.addWidget( checkbox2 )
         hboxlayout.addWidget( checkbox3 )

         self .button = QtGui.QPushButton( "Ok" )
         hboxlayout.addWidget( self .button )

         self .connect( self .button, QtCore.SIGNAL( 'clicked()' ), self .OnButton )

         self .setLayout( hboxlayout )
     def OnButton( self ):
         if self .radio2.isChecked():
             self .radio2.setText( "haha" )

app = QtGui.QApplication( sys.argv )
win = Window()
win.show()
app.exec_()