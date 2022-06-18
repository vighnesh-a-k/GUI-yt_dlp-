from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import yt_dlp
ydl_opts = {
    
  
}
resolutions=[]
buttons=[]
URLS=[]
import sys
form=[]
format=0

class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Python ")
 
        # setting geometry
        self.setGeometry(100, 100, 600, 600)
 
        # calling method
        self.UiComponents()
 
        self.resolutions=[]

        self.setStyleSheet("background-color: #a4dbb3;")
        self.show()
 
        
    def UiComponents(self):
        self.label = QLabel(self)
        self.label.setGeometry(100,50,150,30)
        self.label.setText("video URL below")

        
        self.label.setFont(QFont('Arial', 10))

        push1 = QPushButton("enter", self)

        push1.move(100,200)
        self.download = QPushButton("DOWNLOAD", self)
        self.download.move(100,275)
        self.intake=QLineEdit(self)
        self.intake.setGeometry(100,100,250,30)

        self.display=QLabel(self)
        self.display.move(100,250)
        self.cb = QComboBox(self)
        self.cb.addItem("FORMATS")
        self.cb.setGeometry(100,140,300,30)
        
        self.cb.currentIndexChanged.connect(self.selectionchange)
        self.intake.setStyleSheet("QLineEdit"
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")
        self.cb.setStyleSheet("QComboBox"
                                 "{"
                                 
                                 "background : white;"
                                 "}")
        self.download.setStyleSheet("QPushButton"
                                 "{"
                                 
                                 "background : red;"
                                 "}")
        push1.setStyleSheet("QPushButton"
                                 "{"
                                 
                                 "background : white;"
                                 "}")
        push1.clicked.connect(self.action1)
        self.download.clicked.connect(self.downloaded)

    def action1(self):

       
        URLS.append(self.intake.text())
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(URLS[0], download=False)
        formats=meta.get('formats', [meta])
        for i in range(len(formats)):

            self.cb.addItem(formats[i]["format"]+formats[i]["resolution"])
            form.append(formats[i])
            
        
    def selectionchange(self,i):
        self.display.setText(str(i))
        format=i

    def downloaded(self):
        ydl_opts["format"]=form[format]["format_id"]
        with yt_dlp.YoutubeDL(ydl_opts) as y:
            y.download(URLS[0])


App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()



 
# start the app
sys.exit(App.exec())