from LockBox import Ui_MainWindow
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
        
        # Connect mouse press and move events for the custom title bar
        self.title_bar.mousePressEvent = self.start_window_drag
        self.title_bar.mouseMoveEvent = self.move_window

        # Home Page button navigation
        self.homepage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(0))
        self.helppage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(1))
        self.dcryptpage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(3))
        self.encryptpage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(2))
        self.visit_website_btn.clicked.connect(lambda: webbrowser.open("https:t.me/surafel_is_here"))
    
    def start_window_drag(self, event: QMouseEvent):
        """Start dragging the window."""
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
            event.accept()
    
    def move_window(self, event: QMouseEvent):
        """Move the window based on mouse movement."""
        if event.buttons() == Qt.LeftButton and self.old_pos:
            # Calculate the offset and move the window
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()
            event.accept()
