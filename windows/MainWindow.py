import cv2 as cv
import os
import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6 import QtGui
import configparser
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize, Qt
import glob
from windows.SplashScreen import SplashScreen


class MainWindow(QWidget):
    """A class representing the main window"""    
    curr_idx = 0
    
    def show_splash_screen(self, config_path):
        config = configparser.ConfigParser()
        config.read(config_path)
        splash = SplashScreen()
        splash.show_splash_screen(config)
        return
        
    def set_up(self, config_path):
        """Set up the main window and images"""
        
        # load config and images
        config = configparser.ConfigParser()
        config.read(config_path)
        self._load_images(config)
        
        self.setWindowTitle(config['DEFAULT']['Title'])
        self.setWindowIcon(QtGui.QIcon(config['DEFAULT']['Icon']))
        
        self.left_image = QPixmap(self.images_list[self.curr_idx])
        self.right_image = QPixmap(self.overlays_list[self.curr_idx])
        self.current_label = self.labels_list[self.curr_idx]
        
        self.grid = QGridLayout()
        self.label_right = QLabel()
        self.label_right.setPixmap(self.right_image)
        
        self.label_left = QLabel()
        self.label_left.setPixmap(self.left_image)
        
        self.grid.addWidget(self.label_left,1,1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.label_right,1,3, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.prevBtn = QPushButton(
            icon=QtGui.QIcon(config['DEFAULT']['icon-prev']),
            parent=self
        )
        self.prevBtn.setFixedSize(100, 60)
        self.prevBtn.setIconSize(QSize(80, 40))
        self.prevBtn.clicked.connect(self._set_previous_image)
        
        self.nextBtn = QPushButton(
            icon=QtGui.QIcon(config['DEFAULT']['icon-next']),
            parent=self,
        )
        self.nextBtn.setFixedSize(100, 60)
        self.nextBtn.setIconSize(QSize(80, 40))  
        self.nextBtn.clicked.connect(self._set_next_image)
        
        self.buttons = QHBoxLayout()
        self.buttons.addWidget(self.prevBtn)
        self.buttons.addWidget(self.nextBtn)
        
        self.grid.addLayout(self.buttons,1,2,alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(self.grid)
        self.setGeometry(0,0,int(config['DEFAULT']['size_x']),int(config['DEFAULT']['size_y']))
        self.show()
        return
    
    def _load_images(self, config):
        # ensure the same order
        self.images_list = glob.glob(config['DEFAULT']['images_dir']+"*.png")
        self.overlays_list = glob.glob(config['DEFAULT']['overlays_dir']+"*.png")   
        self.labels_list = glob.glob(config['DEFAULT']['labels_dir']+"*.mat")
        
        self.images_list.sort()
        self.overlays_list.sort()
        self.labels_list.sort()
        return
        
        
    def restart(self):
        self.curr_idx=0
        self.left_image.swap(QPixmap(self.images_list[self.curr_idx]))
        self.right_image.swap(QPixmap(self.overlays_list[self.curr_idx]))
        self.current_label = self.labels_list[self.curr_idx]
        self.show()
        return
    
    def _set_previous_image(self):
        if(self.curr_idx==0):
            self.curr_idx = len(self.images_list)-1
        else:
            self.curr_idx = self.curr_idx-1
        self.left_image.swap(QPixmap(self.images_list[self.curr_idx]))
        self.right_image.swap(QPixmap(self.overlays_list[self.curr_idx]))
        self.label_right.setPixmap(self.right_image)
        self.label_left.setPixmap(self.left_image)
        self.current_label = self.labels_list[self.curr_idx]
        return
    
    def _set_next_image(self):
        if(self.curr_idx==len(self.images_list)-1):
            self.curr_idx = 0
        else:
            self.curr_idx = self.curr_idx+1
        self.left_image.swap(QPixmap(self.images_list[self.curr_idx]))
        self.right_image.swap(QPixmap(self.overlays_list[self.curr_idx]))
        self.label_right.setPixmap(self.right_image)
        self.label_left.setPixmap(self.left_image)
        self.current_label = self.labels_list[self.curr_idx]
        return
    
    
    
    def exit(self):
        pass
    