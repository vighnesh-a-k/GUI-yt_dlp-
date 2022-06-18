from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
import sys

class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Python ")
 
        # setting geometry
        self.setGeometry(100, 100, 360, 350)
 
        # calling method
        self.UiComponents()
 
       
        self.show()
 
        
    def UiComponents(self):
        self.label = QLabel(self)
        self.label.move(100,150,)
        self.label.setText("video URL here")

        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")
        self.label.setFont(QFont('Arial', 15))

        push1 = QPushButton("enter", self)

        push1.move(100,200)

        self.intake=QLineEdit(self)
        self.intake.setGeometry(100,100,200,30)

        self.display=QLabel(self)
        self.display.move(100,250)


        push1.clicked.connect(self.action1)

    def action1(self):

        self.display.setText(self.intake.text())
 

App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())