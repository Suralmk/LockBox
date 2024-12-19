from gui.StarterDialog import Ui_starterDialog
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QPoint

class StartApp(Ui_starterDialog,  QDialog):
    def __init__(self,  parent=None):
        super().__init__()
        self.setupUi(self)

        # Prevent dragging/moving
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)

        self.starterStackWidget.setCurrentIndex(0) 
        self.choose_location_next.clicked.connect(lambda : self.starterStackWidget.setCurrentIndex(1))
        self.passwordpage_next.clicked.connect(lambda : self.starterStackWidget.setCurrentIndex(2))
        self.passphrasepage_next_btn.clicked.connect(self.handle_passphrasepage_next)
        self.recovery_page_next.clicked.connect(lambda : self.starterStackWidget.setCurrentIndex(4))
        self.success_page_next.clicked.connect(lambda: self.accept())
        
        # Center the dialog on the parent
        self.resize(300, 150)
        parent_center = parent.geometry().center()
        self.move(parent_center - QPoint(self.width() // 2, self.height() // 2))

    def handle_passphrasepage_next(self):
         if self.passphrase_backup.isChecked():
              self.starterStackWidget.setCurrentIndex(3)
         else:
              self.starterStackWidget.setCurrentIndex(4)

    def handle_success_start(self):
         self.accept()

    def mousePressEvent(self, event):
            # Override to prevent automatic focus on the close button
            event.ignore()
            super().mousePressEvent(event)