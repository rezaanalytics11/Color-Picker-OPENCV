from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
import numpy as np
import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QFormLayout
from PyQt5.QtCore import Qt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()



        self.label1 = QLabel('', self)
        self.label2 = QLabel('', self)
        self.label3 = QLabel('', self)
        self.label4 = QLabel('Last  RGB  Mixture', self)

        self.label4.setGeometry(30, 230, 200, 100)
        self.label4.setAlignment(Qt.AlignCenter)

        label = QLabel('',self)
        pixmap = QPixmap(r'C:\Users\Ariya Rayaneh\Desktop\result\final result.jpg')
        label.setPixmap(pixmap)
        #self.setCentralWidget(label)
        #label.setAlignment(Qt.AlignCenter)
        label.setGeometry(30, 300, 200, 100)
        self.resize(pixmap.width(), pixmap.height())


        mySlider1 = QSlider(Qt.Horizontal, self)
        mySlider1.setGeometry(30, 40, 200, 30)
        mySlider1.setRange(0, 255)
        self.value1=mySlider1.valueChanged.connect(self.changeValue1)
        mySlider1.setValue(100)

        mySlider2 = QSlider(Qt.Horizontal, self)
        mySlider2.setGeometry(30, 120, 200, 30)
        mySlider2.setRange(0, 255)
        mySlider2.valueChanged.connect(self.changeValue2)
        mySlider2.setValue(100)
        # mySlider2.setSingleStep(5)
        # mySlider2.setPageStep(10)
        # mySlider2.setTickPosition(QSlider.TickPosition.TicksAbove)

        mySlider3 = QSlider(Qt.Horizontal, self)
        mySlider3.setGeometry(30, 200, 200, 30)
        mySlider3.setRange(0, 255)
        mySlider3.valueChanged.connect(self.changeValue3)
        mySlider3.setValue(100)

        self.setGeometry(100, 100, 300, 500)
        self.setWindowTitle("Checkbox Example")
        self.show()




    def changeValue1(self,value):
        self.label1.setText(f'R: {value}')
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setGeometry(30, 5, 200, 50)
        logo1 = np.ones((225, 225, 3), dtype='uint8')* 255
        logo1 = cv2.cvtColor(logo1, cv2.COLOR_BGR2RGB)
        R, G, B = cv2.split(logo1)

        R[0:225, 0:225] = 0
        G[0:225, 0:225] = 0
        B[0:225, 0:225] = value
        result = cv2.merge([R, G, B])
        cv2.imwrite(r'C:\Users\Ariya Rayaneh\Desktop\result\logo1_changeValue1.jpg',result)
        self.draw()

    def changeValue2(self,value):
        self.label2.setText(f'G: {value}')
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setGeometry(30, 95, 200, 30)
        logo1 = np.ones((225, 225, 3), dtype='uint8')
        logo1 = cv2.cvtColor(logo1, cv2.COLOR_BGR2RGB)
        R, G, B = cv2.split(logo1)

        R[0:225, 0:225] = 0
        G[0:225, 0:225] = value
        B[0:225, 0:225] = 0
        result = cv2.merge([R, G, B])

        cv2.imwrite(r'C:\Users\Ariya Rayaneh\Desktop\result\logo1_changeValue2.jpg',result)
        self.draw()

    def changeValue3(self,value):
        self.label3.setText(f'B: {value}')
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setGeometry(30, 175, 200, 30)
        logo1 = np.ones((225, 225, 3), dtype='uint8')
        logo1 = cv2.cvtColor(logo1, cv2.COLOR_BGR2RGB)
        R, G, B = cv2.split(logo1)

        R[0:225, 0:225] = value
        G[0:225, 0:225] = 0
        B[0:225, 0:225] = 0
        result = cv2.merge([R,G,B])
        cv2.imwrite(r'C:\Users\Ariya Rayaneh\Desktop\result\logo1_changeValue3.jpg',result)
        self.draw()


    def draw(self):
        a=cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\result\logo1_changeValue1.jpg')
        b=cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\result\logo1_changeValue2.jpg')
        c=cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\result\logo1_changeValue3.jpg')
        d=a+b+c
        cv2.imshow('output', d)
        cv2.imwrite(r'C:\Users\Ariya Rayaneh\Desktop\result\final result.jpg',d)


if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = Example()
     sys.exit(app.exec_())


