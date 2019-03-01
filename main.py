from PyQt5.QtGui import QPixmap, QTransform, QCursor, QIcon, QImage, QBrush, \
    QPalette, QFont
from PyQt5.QtCore import QTimer, pyqtSignal, QObject, QSize, Qt, QThread, \
    QCoreApplication
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QApplication, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QProgressBar, QGroupBox
from PyQt5.Qt import QTest, QTransform, QSound
import json
from clases import Tab, Buylayout, AddLayout, CheckItem
SCREEN_WIDTH = 768
SCREEN_HEIGHT = 1366
row, col = (SCREEN_HEIGHT*0.05, SCREEN_WIDTH*0.1)
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = [col * x for x in range(1, 11)]
row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row12, row14, row15, row16, row17, row18, row19, row20 = [row * x for x in range(1, 21)]

TABS = ['Agregar Productos', 'Retirar/Consultar', 'Comprar']

class Window(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setGeometry(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.main_layout = AddLayout(self)
        self.show()
        retirar = CheckItem(self)
        comprar = Buylayout(self)
        self.tabs = {}
        with open('db.json') as file:
            self.database = json.load(file)
        for i in range(len(TABS)):
            tab = Tab(self, i, TABS[i], i==0)
            self.tabs[i] = tab

        self.windows = {0: self.main_layout, 1: retirar, 2: comprar}
        self.show()

    def change_tab(self, tab):
        for t_values in self.tabs.values():
            t_values.focused = False
        self.main_layout.hide()
        self.main_layout = self.windows[tab.id]
        self.main_layout.show()
        if isinstance(self.main_layout, Buylayout):
            self.main_layout.code.setFocus()
        elif isinstance(self.main_layout, CheckItem):
            self.main_layout.loadQty(self.main_layout.index)




if __name__ == "__main__":
    app = QApplication([])
    editor = Window()
    app.exec_()
