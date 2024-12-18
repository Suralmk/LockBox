from gui.LockBox import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt, QPoint
import webbrowser

class LockBox(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stack_2.setCurrentIndex(0)

        # Set the window flags to hide the native title bar
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Initialize variables for mouse dragging
        self.old_pos = None

        # Install an event filter on the title bar
        self.title_bar.installEventFilter(self)

        # Home Page button navigation
        self.homepage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(0))
        self.helppage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(1))
        self.dcryptpage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(2))
        self.encryptpage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(3))
        self.visit_website_btn.clicked.connect(lambda: webbrowser.open("https:t.me/surafel_is_here"))

    def eventFilter(self, source, event):
        """Handle mouse press and move events for the title bar."""
        if source == self.title_bar:
            if event.type() == QMouseEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.old_pos = event.globalPosition().toPoint()
                return True
            elif event.type() == QMouseEvent.MouseMove and event.buttons() == Qt.LeftButton:
                if self.old_pos:
                    # Calculate the offset and move the window
                    delta = event.globalPosition().toPoint() - self.old_pos
                    self.move(self.pos() + delta)
                    self.old_pos = event.globalPosition().toPoint()
                return True
        return super().eventFilter(source, event)
