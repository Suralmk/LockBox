from gui.MessageBox import Ui_MessageBox
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QPoint

class MessageBox(Ui_MessageBox,  QDialog):
    def __init__(self, message, parent=None):
        self._message = message
        super().__init__()
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

        #self.message_continue_btn.setFocus()