from gui.MessageBox import Ui_MessageBox
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QPoint

class MessageBox(Ui_MessageBox,  QDialog):
    def __init__(self, message, parent=None):
        self._message = message
        super().__init__(parent)
        self.setupUi(self)

        # Prevent dragging/moving
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)

        self.message_text.setWordWrap(True)

        # Set text alignment to top
        self.message_text.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.message_text.setText(message)

        self.message_continue_btn.clicked.connect(lambda: self.accept())
        self.message_cancel_btn.clicked.connect(lambda: self.close())

        self.center_on_parent(parent)

    def center_on_parent(self, parent):
        """Centers the dialog on the parent widget."""
        if parent:
            parent_center = parent.mapToGlobal(parent.rect().center())
            self.move(parent_center - QPoint(self.width() // 2, self.height() // 2))
        else:
            screen_center = self.screen().geometry().center()
            self.move(screen_center - QPoint(self.width() // 2, self.height() // 2))