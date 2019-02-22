from PyQt5.QtGui import QPixmap, QTransform, QCursor, QIcon, QImage, QBrush, \
    QPalette, QFont
from PyQt5.QtCore import QTimer, pyqtSignal, QObject, QSize, Qt, QThread, \
    QCoreApplication
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QApplication, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QProgressBar, QGroupBox
from PyQt5.Qt import QTest, QTransform, QSound
import wx

app = wx.App(False)
SCREEN_WIDTH, SCREEN_HEIGHT = wx.GetDisplaySize()
SCREEN_WIDTH *= 1.25
SCREEN_HEIGHT *= 1.25

class Window(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        # self.ser = serial.Serial('COM3')
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setGeometry(SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/2 - 250, 500, 500)

        self.label = QLabel("Escanea tu Producto",self)
        self.label.setGeometry(140,100, 300, 50)
        self.label.setFont(QFont("Times",15))

        self.show()

    def listenScan(self):
        self.code = input()
        print(self.code)
        self.label.hide()
        self.newlabel = QLabel(self.code, self)
        self.newlabel.setGeometry(140, 100, 300, 50)
        self.newlabel.setFont(QFont("Times",15))
        self.newlabel.show()







if __name__ == "__main__":
    app = QApplication([])
    editor = Window()
    app.exec_()
