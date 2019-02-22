from PyQt5.QtGui import QPixmap, QTransform, QCursor, QIcon, QImage, QBrush, \
    QPalette, QFont
from PyQt5.QtCore import QTimer, pyqtSignal, QObject, QSize, Qt, QThread, \
    QCoreApplication
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QApplication, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QProgressBar, QGroupBox
from PyQt5.Qt import QTest, QTransform, QSound
import wx, json

app = wx.App(False)
SCREEN_WIDTH, SCREEN_HEIGHT = wx.GetDisplaySize()
SCREEN_WIDTH *= 1.25
SCREEN_HEIGHT *= 1.25

with open('db.json') as file:
    database = json.load(file)

class Window(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        # self.ser = serial.Serial('COM3')
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setGeometry(SCREEN_WIDTH/2 - 450, SCREEN_HEIGHT/2 - 450, 900, 700)

        self.label = QLabel("Escanea tu Producto",self)
        self.label.setGeometry(140,100, 300, 50)
        self.label.setFont(QFont("Times",15))

        self.cart_label = QLabel("Tu Carro", self)
        self.cart_label.setGeometry(520, 15, 380, 30)
        self.cart_label.setFont(QFont("Times",15))

        self.cart_background = QGroupBox(self)
        self.cart_background.setGeometry(500, 0, 400, 700)
        self.cart_background.setStyleSheet('background-color: rgb(100, 200, 100)')
        self.cart_background.lower()

        self.cart_layout = QGroupBox(self)
        self.cart_layout.setGeometry(520, 50, 360, 530)
        self.cart_layout.setStyleSheet('background-color: rgb(255, 255, 255)')

        self.label_total = QLabel("   Total: $0", self)
        self.label_total.setGeometry(520, 580, 360, 100)
        self.label_total.setFont(QFont("Times", 18))
        self.label_total.setStyleSheet('background-color: rgb(255, 255, 255)')

        self.show()

        self.code = QLineEdit(self)
        self.code.setGeometry(0,0,0,0)
        self.code.setFocus()
        self.code.show()

        self.layout = QGroupBox(self)
        self.layout.setGeometry(0,0, 500,700)
        self.layout.lower()

        self.cart = {}
        self.total = 0

        self.boton_cancelar = QPushButton("Cancelar", self)
        self.boton_cancelar.setGeometry(80, 570, 150, 80)
        self.boton_cancelar.setFont(QFont("Times", 18))
        self.boton_cancelar.clicked.connect(self.cancelar)
        self.boton_cancelar.show()

        self.boton_imprimir = QPushButton("Imprimir", self)
        self.boton_imprimir.setGeometry(280, 570, 150, 80)
        self.boton_imprimir.setFont(QFont("Times", 18))
        self.boton_imprimir.show()


    def cancelar(self):
        self.label.show()
        self.layout.hide()
        self.cart = {}
        self.cart_layout.hide()
        self.total = 0

        self.cart_layout = QGroupBox(self)
        self.cart_layout.setGeometry(520, 50, 360, 530)
        self.cart_layout.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.cart_layout.show()

        self.label_total.setText("   Total: ${}".format(str(self.total)))
        self.code.setFocus()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.searchCode()

    def searchCode(self):
        self.label.hide()
        self.layout.hide()

        self.layout = QGroupBox(self)
        self.layout.setGeometry(0,0, 500,700)
        self.layout.lower()
        for i in database:
            if i['Codigo'] == self.code.text():
                label = QLabel('Nombre: ' + i['Nombre'], self.layout)
                label.setGeometry(50, 100, 450, 50)
                label.setFont(QFont("Times", 12))
                label = QLabel('Marca: ' + i['Marca'], self.layout)
                label.setGeometry(50, 200, 450, 50)
                label.setFont(QFont("Times", 12))
                label = QLabel('Precio: $' + i['Precio'], self.layout)
                label.setGeometry(50, 300, 450, 50)
                label.setFont(QFont("Times", 12))
                self.layout.show()
                self.total += int(i['Precio'])
                self.label_total.setText("   Total: ${}".format(str(self.total)))

                if i['Nombre'] in list(self.cart.keys()):
                    self.cart[i['Nombre']][0] += 1
                    self.cart[i['Nombre']][1].setText(str(self.cart[i['Nombre']][0]))
                else:
                    label = QLabel(i['Nombre'], self.cart_layout)
                    label.setGeometry(30, len(self.cart) * 40, 250, 30)
                    label.show()
                    label.setFont(QFont("Times",10))

                    label = QLabel('1', self.cart_layout)
                    label.setGeometry(300, len(self.cart) * 40, 100, 30)
                    label.show()
                    label.setFont(QFont("Times",10))
                    self.cart[i['Nombre']] = [1, label]

        self.code.setText('')

if __name__ == "__main__":
    app = QApplication([])
    editor = Window()
    app.exec_()
