from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QStatusBar
from PyQt6.QtWidgets import QToolBar

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt Lab')

        self.createMenu()
        self.createTabs()

    def createMenu(self):
        self.menu = self.menuBar()
        self.fileMenu = self.menu.addMenu("File")
        self.fileMenu.addAction('Exit', self.close)
        self.fileMenu = self.menu.addMenu("Task 1")
        self.fileMenu.addAction('Open')
        self.fileMenu = self.menu.addMenu("Task 2")
        self.fileMenu.addAction('Clear')
        self.fileMenu.addAction('Open')
        self.fileMenu.addAction('Save')
        self.fileMenu.addAction('Save as')
        self.fileMenu = self.menu.addMenu("Task 3")
        self.fileMenu.addAction('Clear')


    def createTabs(self):
        self.tabs = QTabWidget()

        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()

        self.tabs.addTab(self.tab_1, "Task 1")
        self.tabs.addTab(self.tab_2, "Task 2")
        self.tabs.addTab(self.tab_3, "Task 3")

        self.setCentralWidget(self.tabs)


app = QApplication([])
win = Window()
win.show()
app.exec()
