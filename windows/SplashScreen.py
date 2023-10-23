import time
from PyQt6 import QtGui, QtCore, QtWidgets

class SplashScreen:
    """Splash screen which is displayed at the beginning of the game """
    def show_splash_screen(self, config):
        img = QtGui.QPixmap(config['DEFAULT']['splash_screen'])
        img=img.scaled(int(config['DEFAULT']['size_x']),int(config['DEFAULT']['size_y']),aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.splash = QtWidgets.QSplashScreen(img, QtCore.Qt.WindowType.WindowStaysOnTopHint)
        alpha = 1.0
        step = 0.05
        self.splash.setWindowOpacity(alpha)
        self.splash.show()
        time.sleep(1)
        while alpha > 0:
            self.splash.setWindowOpacity(alpha)
            time.sleep(step)
            alpha-=step
            time.sleep(0.005) 
        self.splash.close() 
    