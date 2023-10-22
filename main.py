import cv2 as cv
import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from windows.MainWindow import MainWindow
from windows.SplashScreen import SplashScreen
import configparser
from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6 import QtGui
import configparser
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize, Qt
import glob
from windows.SplashScreen import SplashScreen
from windows.Help import Help

def main():
    app = QApplication(sys.argv)
    
    config = configparser.ConfigParser()
    config.read("config.ini")
    
    splash = SplashScreen()
    splash.show_splash_screen(config)
    
    game = MainWindow()
    game.set_up(config)
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

