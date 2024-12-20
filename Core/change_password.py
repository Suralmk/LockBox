from gui.ChangePassword import Ui_ChangePassword

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QPoint

class ChangePassword(Ui_ChangePassword,  QDialog):
    def __init__(self,  parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        # Prevent dragging/moving
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.center_on_parent(parent)

    def center_on_parent(self, parent):
        """Centers the dialog on the parent widget."""
        if parent:
            parent_center = parent.mapToGlobal(parent.rect().center())
            self.move(parent_center - QPoint(self.width() // 2, self.height() // 2))
        else:
            screen_center = self.screen().geometry().center()
            self.move(screen_center - QPoint(self.width() // 2, self.height() // 2))