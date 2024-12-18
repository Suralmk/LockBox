import sys
from PySide6.QtWidgets import QApplication
from Core.lock_box import LockBox

app = QApplication(sys.argv)
window = LockBox()
window.show()
app.exec()