import cv2 as cv
import os
import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6 import QtGui
import configparser
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    """A class representing the main window"""    
        
    def set_up(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.setWindowTitle(config['DEFAULT']['Title'])
        self.setWindowIcon(QtGui.QIcon(config['DEFAULT']['Icon']))
        self.resize(int(config['DEFAULT']['size_x']), int(config['DEFAULT']['size_y']))
        self.move(300, 300)
        self.left_image = QPixmap("./Dataset/cpm17/Images/image_00.png")
        self.right_image = QPixmap("./Dataset/cpm17/Overlay/image_00.png")
        
        self.grid = QGridLayout()
        self.label_right = QLabel()
        self.label_right.setPixmap(self.right_image)
        
        self.label_left = QLabel()
        self.label_left.setPixmap(self.left_image)
        
        self.grid.addWidget(self.label_right,1,2)
        self.grid.addWidget(self.label_left,1,1)
        
        
        self.setLayout(self.grid)
        self.setGeometry(50,50,320,200)
        self.show()
    
    def update(self):
        pass
    
    def restart(self):
        pass
    
    def exit(self):
        pass
    