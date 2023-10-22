import time
from PyQt6 import QtGui, QtCore, QtWidgets

class SplashScreen:
    def show_splash_screen(self, config):
        img = QtGui.QPixmap(config['DEFAULT']['splash_screen'])
        self.splash = QtWidgets.QSplashScreen(img, QtCore.Qt.WindowType.WindowStaysOnTopHint)
        alpha = 1.0
        step = 0.2
        self.splash.setWindowOpacity(alpha)
        self.splash.show()
        while alpha > 0:
            self.splash.setWindowOpacity(alpha)
            time.sleep(step)
            alpha-=step
            time.sleep(1) 
        self.splash.close() 
    