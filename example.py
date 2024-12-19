from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QWidget, QPushButton
from PySide6.QtCore import Qt, QPoint, Signal
from PySide6.QtGui import QMouseEvent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        # Add a button to open the dialog
        self.open_dialog_button = QLabel("Click to Open Dialog", self)
        self.open_dialog_button.setGeometry(200, 200, 200, 50)
        self.open_dialog_button.setAlignment(Qt.AlignCenter)
        self.open_dialog_button.setStyleSheet("background-color: lightgray; border: 1px solid black;")
        self.open_dialog_button.mousePressEvent = self.show_dialog

        # Overlay widget for dimmed background
        self.overlay = QWidget(self)
        self.overlay.setGeometry(self.rect())
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.6);")
        self.overlay.hide()

    def show_dialog(self, event):
        self.overlay.show()  # Show dimmed background
        dialog = CustomDialog( self)
        dialog.exec()
        if dialog.result == 0:
            print("here")

class CustomDialog(QDialog):
    # Define a custom signal to notify when the dialog is closed
    closed = Signal()

    def __init__(self,  parent=None):
        super().__init__(parent)

        # Prevent dragging/moving
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)

        # Set the dialog layout
        layout = QVBoxLayout(self)
        label = QLabel("This is a centered modal dialog!", self)
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Close")
        layout.addWidget(button)
        layout.addWidget(label)

        # Connect button to close dialog
        button.clicked.connect(self.close)

        # Center the dialog on the parent
        self.resize(300, 150)
        parent_center = parent.geometry().center()
        self.move(parent_center - QPoint(self.width() // 2, self.height() // 2))

        # Emit the signal when the dialog is closed
        self.closed.connect(self.close)

    def mousePressEvent(self, event: QMouseEvent):
        # Use globalPosition() instead of globalPos() as it is the recommended method
        global_pos = event.globalPosition().toPoint()  # Convert to QPoint
        if  self.geometry().contains(global_pos):
            self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
