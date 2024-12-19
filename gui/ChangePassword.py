# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangePassword.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QWidget)
import resources_rc

class Ui_ChangePassword(object):
    def setupUi(self, ChangePassword):
        if not ChangePassword.objectName():
            ChangePassword.setObjectName(u"ChangePassword")
        ChangePassword.resize(500, 340)
        ChangePassword.setMinimumSize(QSize(500, 340))
        ChangePassword.setMaximumSize(QSize(500, 340))
        ChangePassword.setStyleSheet(u"background:  rgba(35,39,42,1);")
        self.gridLayout = QGridLayout(ChangePassword)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QWidget(ChangePassword)
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

        self.frame = QFrame(ChangePassword)
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
        self.change_password_btn = QPushButton(self.page)
        self.change_password_btn.setObjectName(u"change_password_btn")
        self.change_password_btn.setGeometry(QRect(330, 240, 150, 35))
        self.change_password_btn.setMinimumSize(QSize(150, 35))
        self.change_password_btn.setMaximumSize(QSize(150, 35))
        self.change_password_btn.setMouseTracking(True)
        self.change_password_btn.setStyleSheet(u"background-color: rgba(32,144,46,1);")
        self.change_password_btn.setCheckable(True)
        self.change_password_btn.setChecked(True)
        self.change_password_btn.setAutoExclusive(True)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 152, 20))
        self.label_2.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"")
        self.confirm_password_input = QLineEdit(self.page)
        self.confirm_password_input.setObjectName(u"confirm_password_input")
        self.confirm_password_input.setGeometry(QRect(20, 120, 381, 35))
        self.confirm_password_input.setMinimumSize(QSize(30, 35))
        self.confirm_password_input.setMaximumSize(QSize(16777215, 30))
        self.confirm_password_input.setStyleSheet(u"")
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 90, 152, 21))
        self.label_3.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"")
        self.layoutWidget_2 = QWidget(self.page)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 180, 381, 16))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.very_weak_password_frame = QFrame(self.layoutWidget_2)
        self.very_weak_password_frame.setObjectName(u"very_weak_password_frame")
        self.very_weak_password_frame.setMinimumSize(QSize(50, 10))
        self.very_weak_password_frame.setMaximumSize(QSize(70, 10))
        self.very_weak_password_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.very_weak_password_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.very_weak_password_frame)

        self.week_password_frame = QFrame(self.layoutWidget_2)
        self.week_password_frame.setObjectName(u"week_password_frame")
        self.week_password_frame.setMinimumSize(QSize(50, 10))
        self.week_password_frame.setMaximumSize(QSize(70, 10))
        self.week_password_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.week_password_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.week_password_frame)

        self.medium_password_frame = QFrame(self.layoutWidget_2)
        self.medium_password_frame.setObjectName(u"medium_password_frame")
        self.medium_password_frame.setMinimumSize(QSize(50, 10))
        self.medium_password_frame.setMaximumSize(QSize(70, 10))
        self.medium_password_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.medium_password_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.medium_password_frame)

        self.strong_password_frame = QFrame(self.layoutWidget_2)
        self.strong_password_frame.setObjectName(u"strong_password_frame")
        self.strong_password_frame.setMinimumSize(QSize(50, 10))
        self.strong_password_frame.setMaximumSize(QSize(70, 10))
        self.strong_password_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.strong_password_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.strong_password_frame)

        self.very_strong_password_frame = QFrame(self.layoutWidget_2)
        self.very_strong_password_frame.setObjectName(u"very_strong_password_frame")
        self.very_strong_password_frame.setMinimumSize(QSize(50, 10))
        self.very_strong_password_frame.setMaximumSize(QSize(70, 10))
        self.very_strong_password_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.very_strong_password_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.very_strong_password_frame)

        self.new_password_input = QLineEdit(self.page)
        self.new_password_input.setObjectName(u"new_password_input")
        self.new_password_input.setGeometry(QRect(20, 40, 381, 35))
        self.new_password_input.setMinimumSize(QSize(30, 35))
        self.new_password_input.setMaximumSize(QSize(16777215, 30))
        self.new_password_input.setStyleSheet(u"")
        self.new_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 70, 371, 41))
        self.label_10.setStyleSheet(u"font: 20pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"text-align:center;")
        self.cancel_password_change_btn = QPushButton(self.page_2)
        self.cancel_password_change_btn.setObjectName(u"cancel_password_change_btn")
        self.cancel_password_change_btn.setGeometry(QRect(360, 230, 120, 40))
        self.cancel_password_change_btn.setMinimumSize(QSize(120, 0))
        self.cancel_password_change_btn.setMaximumSize(QSize(120, 40))
        self.cancel_password_change_btn.setMouseTracking(True)
        self.cancel_password_change_btn.setStyleSheet(u"")
        self.cancel_password_change_btn.setCheckable(True)
        self.cancel_password_change_btn.setChecked(True)
        self.cancel_password_change_btn.setAutoExclusive(True)
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(ChangePassword)
        self.close_btn.clicked.connect(ChangePassword.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ChangePassword)
    # setupUi

    def retranslateUi(self, ChangePassword):
        ChangePassword.setWindowTitle(QCoreApplication.translate("ChangePassword", u"Dialog", None))
        self.close_btn.setText("")
        self.change_password_btn.setText(QCoreApplication.translate("ChangePassword", u"Change Password", None))
        self.label_2.setText(QCoreApplication.translate("ChangePassword", u"Current Passowrd", None))
        self.confirm_password_input.setPlaceholderText(QCoreApplication.translate("ChangePassword", u"new password", None))
        self.label_3.setText(QCoreApplication.translate("ChangePassword", u"New Password", None))
        self.new_password_input.setPlaceholderText(QCoreApplication.translate("ChangePassword", u"current password", None))
        self.label_10.setText(QCoreApplication.translate("ChangePassword", u"Password Changed Succesfully", None))
        self.cancel_password_change_btn.setText(QCoreApplication.translate("ChangePassword", u"Cancel", None))
    # retranslateUi

