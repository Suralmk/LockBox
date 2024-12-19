# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ForgotPassphrase.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_ForgotPassPhrase(object):
    def setupUi(self, ForgotPassPhrase):
        if not ForgotPassPhrase.objectName():
            ForgotPassPhrase.setObjectName(u"ForgotPassPhrase")
        ForgotPassPhrase.resize(500, 250)
        ForgotPassPhrase.setMinimumSize(QSize(500, 250))
        ForgotPassPhrase.setMaximumSize(QSize(600, 250))
        ForgotPassPhrase.setStyleSheet(u"background:  rgba(35,39,42,1);")
        self.gridLayout = QGridLayout(ForgotPassPhrase)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QWidget(ForgotPassPhrase)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(500, 40))
        self.title_bar.setMaximumSize(QSize(500, 40))
        self.title_bar.setStyleSheet(u"QWidget {\n"
"border: none;\n"
"}\n"
"QPushButton {\n"
"background:  rgba(35,39,42,1);\n"
"color:white;\n"
"font: 700 14pt \"Segoe UI\";\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background:  rgba(48,50,51,1);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.title_bar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(599, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.close_btn = QPushButton(self.title_bar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(45, 39))
        self.close_btn.setMaximumSize(QSize(40, 39))
        self.close_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/close-large-line.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(15, 15))

        self.gridLayout_2.addWidget(self.close_btn, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.title_bar, 0, 0, 1, 1)

        self.frame = QFrame(ForgotPassPhrase)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QPushButton {\n"
"		text-align:center;\n"
"color:rgba(240, 247, 255,0.7);\n"
"         font-size:15px;\n"
"		padding-left: 15px;\n"
"padding: 7px 10px;\n"
"border:none;\n"
"background-color: rgba(55, 61, 56, 1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(240, 247, 255,0.1);\n"
"}\n"
"\n"
"QLineEdit {\n"
"border-radius:5px;\n"
"border: 1px solid rgba(102,102,102,1);\n"
"background: rgba(35,39,42,1);\n"
"padding-left: 15px;\n"
"color: white;\n"
"}\n"
"\n"
"QFrame {\n"
"background :rgba(102,102,102,1);\n"
"}\n"
"\n"
"\n"
"/*  QTextEdit Styles */\n"
"QTextEdit {\n"
"border-radius:5px;\n"
"border: 1px solid rgba(102,102,102,1);\n"
"background: rgba(35,39,42,1);\n"
"padding-left: 15px;\n"
"color: white;\n"
"}\n"
"\n"
"    QTextEdit QScrollBar:vertical {\n"
"        width: 10px; /* Decrease the width of the scrollbar */\n"
"        background:  rgba(35,39,42,1); /* Set the background color to black */\n"
"    }\n"
"    QTextEdit QScrollBar:handle:vertical {\n"
"        background: rgba(102,102,102,1"
                        "); /* Handle color - dark gray */\n"
"        border-radius: 5px; /* Optional rounded corners */\n"
"    }\n"
"    QTextEdit QScrollBar:add-line:vertical, QTextEdit QScrollBar:sub-line:vertical {\n"
"        border: none; /* Hide the add/sub buttons */\n"
"    }\n"
"    QTextEdit QScrollBar:up-arrow:vertical, QTextEdit QScrollBar:down-arrow:vertical {\n"
"        border: none;\n"
"        background: none;\n"
"    }")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 0, 271, 20))
        self.label_9.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"")
        self.recovery_phrase_text_field = QTextEdit(self.page)
        self.recovery_phrase_text_field.setObjectName(u"recovery_phrase_text_field")
        self.recovery_phrase_text_field.setGeometry(QRect(20, 30, 461, 101))
        self.copy_recovery_phrase_btn = QPushButton(self.page)
        self.copy_recovery_phrase_btn.setObjectName(u"copy_recovery_phrase_btn")
        self.copy_recovery_phrase_btn.setGeometry(QRect(20, 150, 120, 34))
        self.copy_recovery_phrase_btn.setMaximumSize(QSize(120, 40))
        self.copy_recovery_phrase_btn.setMouseTracking(True)
        self.copy_recovery_phrase_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/file-copy-line (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.copy_recovery_phrase_btn.setIcon(icon1)
        self.copy_recovery_phrase_btn.setCheckable(True)
        self.copy_recovery_phrase_btn.setChecked(True)
        self.copy_recovery_phrase_btn.setAutoExclusive(True)
        self.recovery_page_next = QPushButton(self.page)
        self.recovery_page_next.setObjectName(u"recovery_page_next")
        self.recovery_page_next.setGeometry(QRect(360, 150, 120, 35))
        self.recovery_page_next.setMinimumSize(QSize(120, 35))
        self.recovery_page_next.setMaximumSize(QSize(120, 35))
        self.recovery_page_next.setMouseTracking(True)
        self.recovery_page_next.setStyleSheet(u"background-color: rgba(32,144,46,1);")
        self.recovery_page_next.setCheckable(True)
        self.recovery_page_next.setChecked(True)
        self.recovery_page_next.setAutoExclusive(True)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(190, 10, 131, 20))
        self.label_10.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"")
        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 40, 321, 111))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.passphrase_show_input = QTextEdit(self.widget)
        self.passphrase_show_input.setObjectName(u"passphrase_show_input")
        self.passphrase_show_input.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.passphrase_show_input)

        self.copy_passphrase_btn = QPushButton(self.widget)
        self.copy_passphrase_btn.setObjectName(u"copy_passphrase_btn")
        self.copy_passphrase_btn.setMinimumSize(QSize(120, 0))
        self.copy_passphrase_btn.setMaximumSize(QSize(120, 40))
        self.copy_passphrase_btn.setMouseTracking(True)
        self.copy_passphrase_btn.setStyleSheet(u"")
        self.copy_passphrase_btn.setIcon(icon1)
        self.copy_passphrase_btn.setCheckable(True)
        self.copy_passphrase_btn.setChecked(True)
        self.copy_passphrase_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.copy_passphrase_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(ForgotPassPhrase)
        self.close_btn.clicked.connect(ForgotPassPhrase.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ForgotPassPhrase)
    # setupUi

    def retranslateUi(self, ForgotPassPhrase):
        ForgotPassPhrase.setWindowTitle(QCoreApplication.translate("ForgotPassPhrase", u"Dialog", None))
        self.close_btn.setText("")
        self.label_9.setText(QCoreApplication.translate("ForgotPassPhrase", u"Enter secret  recovery phrase", None))
        self.copy_recovery_phrase_btn.setText(QCoreApplication.translate("ForgotPassPhrase", u"Copy", None))
        self.recovery_page_next.setText(QCoreApplication.translate("ForgotPassPhrase", u"Next", None))
        self.label_10.setText(QCoreApplication.translate("ForgotPassPhrase", u"Your Passphrase", None))
        self.copy_passphrase_btn.setText(QCoreApplication.translate("ForgotPassPhrase", u"Copy", None))
    # retranslateUi

