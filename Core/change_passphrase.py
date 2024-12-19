from gui.ChangePassphrase import Ui_ForgotPassPhrase

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QPoint

class ChangePassphrase(Ui_ForgotPassPhrase, QDialog):
    def __init__(self,  parent=None):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        # Prevent dragging/moving
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)

        self.resize(300, 150)
        parent_center = parent.geometry().center()
        self.move(parent_center - QPoint(self.width() // 2, self.height() // 2))