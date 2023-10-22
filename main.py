import cv2 as cv
import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from windows.MainWindow import MainWindow
import configparser

def main():
    app = QApplication(sys.argv)
    game = MainWindow()
    game.show_splash_screen("config.ini")
    game.set_up("config.ini")
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

