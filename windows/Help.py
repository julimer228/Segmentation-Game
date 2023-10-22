from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
import time

class Help(QDialog):
    """Help window with the short information about the game"""
    def __init__(self, config):
        super().__init__()
        self.config=config
    
    def display_help(self):
        self.setWindowTitle("Instrukcja")
        app_icon = QtGui.QIcon()
        app_icon.addFile(self.config['DEFAULT']['Icon'])
        self.setWindowIcon(app_icon)
        self.exec()
        return
    