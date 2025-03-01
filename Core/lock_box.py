from gui.LockBox import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidget
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt, QPoint
import webbrowser
from Core.start_app import StartApp
from .message import MessageBox
from .change_password import ChangePassword
from .change_passphrase import ChangePassphrase
from Auth.auth import LockBoxAuth

class LockBox(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stack_1.setCurrentIndex(0)
        self.stack_2.setCurrentIndex(0)

        #Initialize LockBox auth instance
        self.auth = LockBoxAuth()
        if not self.auth.user_exists():
            #self.show_start_app_dialog() 
            self.stack_1.setCurrentIndex(0)

        # Overlay when dialog opens
        self.overlay = QWidget(self)
        self.overlay.setGeometry(self.rect())
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")
        self.overlay.setVisible(False)

        # Set the window flags to hide the native title ba
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Initialize variables for mouse dragging
        self.old_pos = None

        # Install an event filter on the title bar
        self.title_bar.installEventFilter(self)

        # LockBox Login
        self.stack_1_login_btn.clicked.connect(self.handle_lockbox_login)

        # Home Page button navigation
        self.homepage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(0))
        self.helppage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(1))
        self.dcryptpage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(2))
        self.encryptpage_btn.clicked.connect(lambda: self.stack_2.setCurrentIndex(3))
        self.visit_website_btn.clicked.connect(lambda: webbrowser.open("https:t.me/surafel_is_here"))

        self.landingpage_get_started_btn.clicked.connect(self.handle_start_app)

        #Handle Change Password
        self.change_password_btn.clicked.connect(self.handle_password_change)
        self.change_passphrase_btn.clicked.connect(self.handle_passphrase_change)

    def handle_password_change(self):
        change_password_dialog = ChangePassword(self)
        self.overlay.setVisible(True)
        result = change_password_dialog.exec()
        if int(result) == 1:
            self.stack_1.setCurrentIndex(1)
        else:
            pass
        
        self.overlay.setVisible(False)

    def handle_passphrase_change(self):
        change_passphrase_dialog = ChangePassphrase(self)
        self.overlay.setVisible(True)
        result = change_passphrase_dialog.exec()
        if int(result) == 1:
            self.stack_1.setCurrentIndex(1)
        else:
            pass

        self.overlay.setVisible(False)

    def handle_start_app(self):
        start_app = StartApp(self)
        self.overlay.setVisible(True)
        result = start_app.exec()
        if int(result) == 1:
            self.stack_1.setCurrentIndex(1)
        else:
            pass
        self.overlay.setVisible(False)

    def handle_lockbox_login(self):
        password = self.stack_1_password_input.text()

        if self.auth.authenticate_user(password):
            self.stack_1.setCurrentIndex(2)
            self.show_message("Welcome to the club, you're a real super user here!")
        else:
            self.show_message("Login failed: Incorrect username or password.")


    def show_message(self,message):
        message_box = MessageBox(message)
        result = message_box.exec()
        if int(result) == 1:
            print("yes")
        else:
            print("no")
        
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
