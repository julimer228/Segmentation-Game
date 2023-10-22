import cv2 as cv
import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from windows.MainWindow import MainWindow
import configparser

def main():
    app = QApplication(sys.argv)
    game = MainWindow()
    game.set_up()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

