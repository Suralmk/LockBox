from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QAction

class Dialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(0, 0, 500, 500)

        menu = self.menuBar()
        submenu = menu.addMenu("Submenu")
        self.action_open_dialog = QAction("Open Dialog", self)
        self.action_open_dialog.setCheckable(False)
        self.action_open_dialog.triggered.connect(self.open_dialog)
        submenu.addAction(self.action_open_dialog)

    def open_dialog(self):
        dialog = Dialog(self)
        dialog.exec()

if __name__ == '__main__':

    app = QApplication()
    w = MainWindow()
    w.show()
    app.exec()