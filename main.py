from PyQt5.QtGui import QPixmap, QTransform, QCursor, QIcon, QImage, QBrush, \
    QPalette, QFont
from PyQt5.QtCore import QTimer, pyqtSignal, QObject, QSize, Qt, QThread, \
    QCoreApplication
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QApplication, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QProgressBar, QGroupBox
from PyQt5.Qt import QTest, QTransform, QSound
import json
SCREEN_WIDTH = 768
SCREEN_HEIGHT = 1366

with open('db.json') as file:
    database = json.load(file)

class Window(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setGeometry(0,0, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.label = QLabel("Escanea tu Producto", self)
        self.label.setGeometry(270, 200, 300, 50)
        self.label.setFont(QFont("Times",18))

        self.cart_label = QLabel("Tu Carro", self)
        self.cart_label.setGeometry(20, 515, 150, 40)
        self.cart_label.setFont(QFont("Times", 15))

        self.cart_background = QGroupBox(self)
        self.cart_background.setGeometry(0, 500, 768, 866)
        self.cart_background.setStyleSheet('background-color: rgb(100,255,100)')
        self.cart_background.lower()

        self.cart_layout = QGroupBox(self)
        self.cart_layout.setGeometry(20, 560, 728, 786)
        self.cart_layout.setStyleSheet('background-color: white')


        self.layout = QGroupBox(self)
        self.layout.setGeometry(0,0, 768,500)
        self.layout.lower()

        self.code = QLineEdit(self)
        self.code.setGeometry(0,0,0,0)
        self.code.setFocus()

        self.cart = {}
        self.total = 0

        self.label_total = QLabel("   Total: $0", self)
        self.label_total.setGeometry(20, 1250, 328, 90)
        self.label_total.setFont(QFont("Times", 20))
        self.label_total.setStyleSheet('background-color: rgb(255, 255, 255)')

        self.boton_cancelar = QPushButton("Cancelar", self)
        self.boton_cancelar.setGeometry(300, 1250, 200, 90)
        self.boton_cancelar.setFont(QFont("Times", 18))
        self.boton_cancelar.clicked.connect(self.cancelar)

        self.boton_imprimir = QPushButton("Imprimir", self)
        self.boton_imprimir.setGeometry(500, 1250, 200, 90)
        self.boton_imprimir.setFont(QFont("Times", 18))

        self.icono = QLabel(self)
        self.icono.setPixmap(QPixmap('logo.svg').scaled(300, 100))
        self.icono.move(234, 50)

        self.show()

    def cancelar(self):
        self.label.show()
        self.layout.hide()
        self.cart = {}
        self.cart_layout.hide()
        self.total = 0

        self.cart_layout = QGroupBox(self)
        self.cart_layout.setGeometry(20, 560, 728, 786)
        self.cart_layout.lower()
        self.cart_background.lower()
        self.cart_layout.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.cart_layout.show()

        self.label_total.setText("   Total: ${}".format(str(self.total)))
        self.code.setFocus()

    def keyPressEvent(self, event):
        self.searchCode()

    def mousePressEvent(self, event):
        self.code.setFocus()

    def searchCode(self):
        self.label.hide()
        self.layout.hide()

        self.layout = QGroupBox(self)
        self.layout.setGeometry(0,0, 768, 500)
        self.layout.lower()
        for i in database:
            if i['Codigo'] == self.code.text():
                label = QLabel('Nombre: ' + i['Nombre'], self.layout)
                label.setGeometry(20, 250, 450, 50)
                label.setFont(QFont("Times", 16))
                label = QLabel('Marca: ' + i['Marca'], self.layout)
                label.setGeometry(20, 340, 450, 50)
                label.setFont(QFont("Times", 16))
                label = QLabel('Precio: $' + i['Precio'], self.layout)
                label.setGeometry(20, 430, 450, 50)
                label.setFont(QFont("Times", 16))
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
                    label.setFont(QFont("Times",13))

                    label = QLabel('1', self.cart_layout)
                    label.setGeometry(300, len(self.cart) * 40, 100, 30)
                    label.show()
                    label.setFont(QFont("Times",13))
                    self.cart[i['Nombre']] = [1, label]

        self.code.setText('')


if __name__ == "__main__":
    app = QApplication([])
    editor = Window()
    app.exec_()
