from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create a QLabel with long text
        label = QLabel(
            "This is a very long text that should wrap to the next line when it exceeds the width of the QLabel."
        )
        
        # Enable word wrap
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Optional: Set fixed width for demonstration
        label.setFixedWidth(300)

        # Style the QLabel (optional)
        label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #333;
                border: 1px solid #ccc;
                padding: 5px;
            }
        """)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        self.setWindowTitle("QLabel Word Wrap Example")
        self.resize(400, 200)


# Run the application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
