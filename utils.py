import time
from PyQt6 import QtGui, QtCore, QtWidgets
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    # Create splashscreen
    splash_pix = QtGui.QPixmap('picture.png')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowType.WindowStaysOnTopHint)
    # add fade to splashscreen 
    opaqueness = 0.0
    step = 0.1
    splash.setWindowOpacity(opaqueness)
    splash.show()
    while opaqueness < 1:
        splash.setWindowOpacity(opaqueness)
        time.sleep(step) # Gradually appears
        opaqueness+=step
    time.sleep(1) # hold image on screen for a while
    splash.close() # close the splash screen
    #widget = YourWidget()
    #widget.show() # This is where you'd run the normal application
    app.exec_()