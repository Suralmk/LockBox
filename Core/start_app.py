from gui.StarterDialog import Ui_starterDialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, QPoint

class StartApp(Ui_starterDialog, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Prevent dragging/moving
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)

        # Initialize stack widget
        self.starterStackWidget.setCurrentIndex(0)
        self.choose_location_next.clicked.connect(lambda: self.starterStackWidget.setCurrentIndex(1))
        self.passwordpage_next.clicked.connect(lambda: self.starterStackWidget.setCurrentIndex(2))
        self.passphrasepage_next_btn.clicked.connect(self.handle_passphrasepage_next)
        self.recovery_page_next.clicked.connect(lambda: self.starterStackWidget.setCurrentIndex(4))
        self.success_page_next.clicked.connect(lambda: self.accept())

        # Resize and center the dialog on the parent
        self.resize(300, 150)
        self.center_on_parent(parent)

    def center_on_parent(self, parent):
        """Centers the dialog on the parent widget."""
        if parent:
            parent_center = parent.mapToGlobal(parent.rect().center())
            self.move(parent_center - QPoint(self.width() // 2, self.height() // 2))
        else:
            screen_center = self.screen().geometry().center()
            self.move(screen_center - QPoint(self.width() // 2, self.height() // 2))

    def handle_passphrasepage_next(self):
        """Handles the passphrase page navigation."""
        if self.passphrase_backup.isChecked():
            self.starterStackWidget.setCurrentIndex(3)
        else:
            self.starterStackWidget.setCurrentIndex(4)

    def handle_success_start(self):
        """Handles success start action."""
        self.accept()

    def mousePressEvent(self, event):
        """Overrides mouse press event to prevent default behavior."""
        event.ignore()
        super().mousePressEvent(event)
