# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StarterDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_starterDialog(object):
    def setupUi(self, starterDialog):
        if not starterDialog.objectName():
            starterDialog.setObjectName(u"starterDialog")
        starterDialog.resize(600, 350)
        starterDialog.setMinimumSize(QSize(600, 350))
        starterDialog.setMaximumSize(QSize(600, 350))
        starterDialog.setStyleSheet(u"background:  rgba(35,39,42,1);")
        self.gridLayout = QGridLayout(starterDialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QWidget(starterDialog)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(600, 40))
        self.title_bar.setMaximumSize(QSize(16777215, 40))
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

        self.frame = QFrame(starterDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.starterStackWidget = QStackedWidget(self.frame)
        self.starterStackWidget.setObjectName(u"starterStackWidget")
        self.starterStackWidget.setStyleSheet(u"QPushButton {\n"
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
        self.filelocationpage = QWidget()
        self.filelocationpage.setObjectName(u"filelocationpage")
        self.choose_location_next = QPushButton(self.filelocationpage)
        self.choose_location_next.setObjectName(u"choose_location_next")
        self.choose_location_next.setGeometry(QRect(460, 250, 120, 35))
        self.choose_location_next.setMaximumSize(QSize(16777215, 40))
        self.choose_location_next.setMouseTracking(True)
        self.choose_location_next.setStyleSheet(u"background-color: rgba(32,144,46,1);")
        self.choose_location_next.setCheckable(True)
        self.choose_location_next.setChecked(True)
        self.choose_location_next.setAutoExclusive(True)
        self.layoutWidget = QWidget(self.filelocationpage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 551, 131))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgb(240, 247, 255);\n"
"background:transparent;\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.choose_location_btn = QPushButton(self.layoutWidget)
        self.choose_location_btn.setObjectName(u"choose_location_btn")
        self.choose_location_btn.setMaximumSize(QSize(16777215, 40))
        self.choose_location_btn.setMouseTracking(True)
        self.choose_location_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/folder-3-fill.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.choose_location_btn.setIcon(icon1)
        self.choose_location_btn.setCheckable(True)
        self.choose_location_btn.setChecked(True)
        self.choose_location_btn.setAutoExclusive(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.choose_location_btn)

        self.choose_location_input = QLineEdit(self.layoutWidget)
        self.choose_location_input.setObjectName(u"choose_location_input")
        self.choose_location_input.setMinimumSize(QSize(30, 35))
        self.choose_location_input.setMaximumSize(QSize(16777215, 30))
        self.choose_location_input.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.choose_location_input)


        self.verticalLayout.addLayout(self.formLayout)

        self.starterStackWidget.addWidget(self.filelocationpage)
        self.createpasswordpage = QWidget()
        self.createpasswordpage.setObjectName(u"createpasswordpage")
        self.passwordpage_next = QPushButton(self.createpasswordpage)
        self.passwordpage_next.setObjectName(u"passwordpage_next")
        self.passwordpage_next.setGeometry(QRect(460, 250, 120, 35))
        self.passwordpage_next.setMinimumSize(QSize(120, 35))
        self.passwordpage_next.setMaximumSize(QSize(120, 35))
        self.passwordpage_next.setMouseTracking(True)
        self.passwordpage_next.setStyleSheet(u"background-color: rgba(32,144,46,1);")
        self.passwordpage_next.setCheckable(True)
        self.passwordpage_next.setChecked(True)
        self.passwordpage_next.setAutoExclusive(True)
        self.label_3 = QLabel(self.createpasswordpage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 89, 152, 21))
        self.label_3.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgb(240, 247, 255);\n"
"background:transparent;\n"
"")
        self.password_strngth_label = QLabel(self.createpasswordpage)
        self.password_strngth_label.setObjectName(u"password_strngth_label")
        self.password_strngth_label.setGeometry(QRect(450, 190, 81, 16))
        self.password_strngth_label.setStyleSheet(u"background:none;\n"
"color:white;")
        self.passwordppage_back = QPushButton(self.createpasswordpage)
        self.passwordppage_back.setObjectName(u"passwordppage_back")
        self.passwordppage_back.setGeometry(QRect(20, 250, 120, 34))
        self.passwordppage_back.setMaximumSize(QSize(120, 40))
        self.passwordppage_back.setMouseTracking(True)
        self.passwordppage_back.setStyleSheet(u"")
        self.passwordppage_back.setCheckable(True)
        self.passwordppage_back.setChecked(True)
        self.passwordppage_back.setAutoExclusive(True)
        self.label_2 = QLabel(self.createpasswordpage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 0, 152, 20))
        self.label_2.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgb(240, 247, 255);\n"
"background:transparent;\n"
"")
        self.new_password_input = QLineEdit(self.createpasswordpage)
        self.new_password_input.setObjectName(u"new_password_input")
        self.new_password_input.setGeometry(QRect(20, 32, 381, 35))
        self.new_password_input.setMinimumSize(QSize(30, 35))
        self.new_password_input.setMaximumSize(QSize(16777215, 30))
        self.new_password_input.setStyleSheet(u"")
        self.confirm_password_input = QLineEdit(self.createpasswordpage)
        self.confirm_password_input.setObjectName(u"confirm_password_input")
        self.confirm_password_input.setGeometry(QRect(20, 122, 381, 35))
        self.confirm_password_input.setMinimumSize(QSize(30, 35))
        self.confirm_password_input.setMaximumSize(QSize(16777215, 30))
        self.confirm_password_input.setStyleSheet(u"")
        self.layoutWidget1 = QWidget(self.createpasswordpage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 182, 381, 16))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.very_weak_password_frame = QFrame(self.layoutWidget1)
        self.very_weak_password_frame.setObjectName(u"very_weak_password_frame")
        self.very_weak_password_frame.setMinimumSize(QSize(50, 10))
        self.very_weak_password_frame.setMaximumSize(QSize(70, 10))
        self.very_weak_password_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.very_weak_password_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.very_weak_password_frame)

        self.week_password_frame = QFrame(self.layoutWidget1)
        self.week_password_frame.setObjectName(u"week_password_frame")
        self.week_password_frame.setMinimumSize(QSize(50, 10))
        self.week_password_frame.setMaximumSize(QSize(70, 10))
        self.week_password_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.week_password_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.week_password_frame)

        self.medium_password_frame = QFrame(self.layoutWidget1)
        self.medium_password_frame.setObjectName(u"medium_password_frame")
        self.medium_password_frame.setMinimumSize(QSize(50, 10))
        self.medium_password_frame.setMaximumSize(QSize(70, 10))
        self.medium_password_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.medium_password_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.medium_password_frame)

        self.strong_password_frame = QFrame(self.layoutWidget1)
        self.strong_password_frame.setObjectName(u"strong_password_frame")
        self.strong_password_frame.setMinimumSize(QSize(50, 10))
        self.strong_password_frame.setMaximumSize(QSize(70, 10))
        self.strong_password_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.strong_password_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.strong_password_frame)

        self.very_strong_password_frame = QFrame(self.layoutWidget1)
        self.very_strong_password_frame.setObjectName(u"very_strong_password_frame")
        self.very_strong_password_frame.setMinimumSize(QSize(50, 10))
        self.very_strong_password_frame.setMaximumSize(QSize(70, 10))
        self.very_strong_password_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.very_strong_password_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.very_strong_password_frame)

        self.starterStackWidget.addWidget(self.createpasswordpage)
        self.createpassphrasepage = QWidget()
        self.createpassphrasepage.setObjectName(u"createpassphrasepage")
        self.label_7 = QLabel(self.createpassphrasepage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 0, 152, 20))
        self.label_7.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"")
        self.new_passphrase = QLineEdit(self.createpassphrasepage)
        self.new_passphrase.setObjectName(u"new_passphrase")
        self.new_passphrase.setGeometry(QRect(20, 32, 380, 35))
        self.new_passphrase.setMinimumSize(QSize(30, 35))
        self.new_passphrase.setMaximumSize(QSize(16777215, 30))
        self.new_passphrase.setStyleSheet(u"")
        self.passphrasepage_next_btn = QPushButton(self.createpassphrasepage)
        self.passphrasepage_next_btn.setObjectName(u"passphrasepage_next_btn")
        self.passphrasepage_next_btn.setGeometry(QRect(460, 250, 120, 35))
        self.passphrasepage_next_btn.setMinimumSize(QSize(120, 35))
        self.passphrasepage_next_btn.setMaximumSize(QSize(120, 35))
        self.passphrasepage_next_btn.setMouseTracking(True)
        self.passphrasepage_next_btn.setStyleSheet(u"background-color: rgba(32,144,46,1);")
        self.passphrasepage_next_btn.setCheckable(True)
        self.passphrasepage_next_btn.setChecked(True)
        self.passphrasepage_next_btn.setAutoExclusive(True)
        self.label_8 = QLabel(self.createpassphrasepage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 89, 152, 21))
        self.label_8.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"")
        self.confirm_passphrase = QLineEdit(self.createpassphrasepage)
        self.confirm_passphrase.setObjectName(u"confirm_passphrase")
        self.confirm_passphrase.setGeometry(QRect(20, 122, 380, 35))
        self.confirm_passphrase.setMinimumSize(QSize(30, 35))
        self.confirm_passphrase.setMaximumSize(QSize(16777215, 30))
        self.confirm_passphrase.setStyleSheet(u"")
        self.passphrasepage_back_btn = QPushButton(self.createpassphrasepage)
        self.passphrasepage_back_btn.setObjectName(u"passphrasepage_back_btn")
        self.passphrasepage_back_btn.setGeometry(QRect(20, 250, 120, 34))
        self.passphrasepage_back_btn.setMaximumSize(QSize(120, 40))
        self.passphrasepage_back_btn.setMouseTracking(True)
        self.passphrasepage_back_btn.setStyleSheet(u"")
        self.passphrasepage_back_btn.setCheckable(True)
        self.passphrasepage_back_btn.setChecked(True)
        self.passphrasepage_back_btn.setAutoExclusive(True)
        self.generate_passphrase_btn = QPushButton(self.createpassphrasepage)
        self.generate_passphrase_btn.setObjectName(u"generate_passphrase_btn")
        self.generate_passphrase_btn.setGeometry(QRect(420, 30, 120, 34))
        self.generate_passphrase_btn.setMaximumSize(QSize(120, 40))
        self.generate_passphrase_btn.setMouseTracking(True)
        self.generate_passphrase_btn.setStyleSheet(u"")
        self.generate_passphrase_btn.setCheckable(True)
        self.generate_passphrase_btn.setChecked(True)
        self.generate_passphrase_btn.setAutoExclusive(True)
        self.passphrase_backup = QRadioButton(self.createpassphrasepage)
        self.passphrase_backup.setObjectName(u"passphrase_backup")
        self.passphrase_backup.setGeometry(QRect(30, 180, 201, 20))
        self.passphrase_backup.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"")
        self.starterStackWidget.addWidget(self.createpassphrasepage)
        self.recoveryphrasepage = QWidget()
        self.recoveryphrasepage.setObjectName(u"recoveryphrasepage")
        self.recovery_phrase_text_field = QTextEdit(self.recoveryphrasepage)
        self.recovery_phrase_text_field.setObjectName(u"recovery_phrase_text_field")
        self.recovery_phrase_text_field.setGeometry(QRect(20, 30, 380, 101))
        self.copy_recovery_phrase_btn = QPushButton(self.recoveryphrasepage)
        self.copy_recovery_phrase_btn.setObjectName(u"copy_recovery_phrase_btn")
        self.copy_recovery_phrase_btn.setGeometry(QRect(280, 140, 120, 34))
        self.copy_recovery_phrase_btn.setMaximumSize(QSize(120, 40))
        self.copy_recovery_phrase_btn.setMouseTracking(True)
        self.copy_recovery_phrase_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/file-copy-line (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.copy_recovery_phrase_btn.setIcon(icon2)
        self.copy_recovery_phrase_btn.setCheckable(True)
        self.copy_recovery_phrase_btn.setChecked(True)
        self.copy_recovery_phrase_btn.setAutoExclusive(True)
        self.label_9 = QLabel(self.recoveryphrasepage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 0, 271, 20))
        self.label_9.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"")
        self.label_10 = QLabel(self.recoveryphrasepage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 200, 421, 20))
        self.label_10.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"")
        self.label_11 = QLabel(self.recoveryphrasepage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 220, 191, 20))
        self.label_11.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"")
        self.recovery_page_baxk = QPushButton(self.recoveryphrasepage)
        self.recovery_page_baxk.setObjectName(u"recovery_page_baxk")
        self.recovery_page_baxk.setGeometry(QRect(20, 250, 120, 34))
        self.recovery_page_baxk.setMaximumSize(QSize(120, 40))
        self.recovery_page_baxk.setMouseTracking(True)
        self.recovery_page_baxk.setStyleSheet(u"")
        self.recovery_page_baxk.setCheckable(True)
        self.recovery_page_baxk.setChecked(True)
        self.recovery_page_baxk.setAutoExclusive(True)
        self.recovery_page_next = QPushButton(self.recoveryphrasepage)
        self.recovery_page_next.setObjectName(u"recovery_page_next")
        self.recovery_page_next.setGeometry(QRect(460, 250, 120, 35))
        self.recovery_page_next.setMinimumSize(QSize(120, 35))
        self.recovery_page_next.setMaximumSize(QSize(120, 35))
        self.recovery_page_next.setMouseTracking(True)
        self.recovery_page_next.setStyleSheet(u"background-color: rgba(32,144,46,1);")
        self.recovery_page_next.setCheckable(True)
        self.recovery_page_next.setChecked(True)
        self.recovery_page_next.setAutoExclusive(True)
        self.starterStackWidget.addWidget(self.recoveryphrasepage)
        self.successpage = QWidget()
        self.successpage.setObjectName(u"successpage")
        self.success_page_next = QPushButton(self.successpage)
        self.success_page_next.setObjectName(u"success_page_next")
        self.success_page_next.setGeometry(QRect(460, 250, 120, 35))
        self.success_page_next.setMinimumSize(QSize(120, 35))
        self.success_page_next.setMaximumSize(QSize(120, 35))
        self.success_page_next.setMouseTracking(True)
        self.success_page_next.setStyleSheet(u"background-color: rgba(32,144,46,1);")
        self.success_page_next.setCheckable(True)
        self.success_page_next.setChecked(True)
        self.success_page_next.setAutoExclusive(True)
        self.layoutWidget2 = QWidget(self.successpage)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(200, 40, 209, 156))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.layoutWidget2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(120, 120))
        self.frame_2.setMaximumSize(QSize(120, 120))
        self.frame_2.setStyleSheet(u"border-radius:50%;\n"
"background-color: rgba(32,144,46,1);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QSize(61, 71))
        self.label_12.setPixmap(QPixmap(u":/icons/icons/check-line.png"))
        self.label_12.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_13 = QLabel(self.layoutWidget2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color:rgb(240, 247, 255);\n"
"background:transparent;\n"
"font-weight:bold\n"
"")

        self.verticalLayout_3.addWidget(self.label_13)

        self.starterStackWidget.addWidget(self.successpage)

        self.gridLayout_3.addWidget(self.starterStackWidget, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(starterDialog)
        self.close_btn.clicked.connect(starterDialog.close)

        self.starterStackWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(starterDialog)
    # setupUi

    def retranslateUi(self, starterDialog):
        starterDialog.setWindowTitle(QCoreApplication.translate("starterDialog", u"Dialog", None))
        self.close_btn.setText("")
        self.choose_location_next.setText(QCoreApplication.translate("starterDialog", u"Next", None))
        self.label.setText(QCoreApplication.translate("starterDialog", u"Where should Lockbox store the encrypted files?", None))
        self.choose_location_btn.setText(QCoreApplication.translate("starterDialog", u"Choose Location", None))
        self.choose_location_input.setPlaceholderText(QCoreApplication.translate("starterDialog", u"Location", None))
        self.passwordpage_next.setText(QCoreApplication.translate("starterDialog", u"Next", None))
        self.label_3.setText(QCoreApplication.translate("starterDialog", u"Confirm Password", None))
        self.password_strngth_label.setText("")
        self.passwordppage_back.setText(QCoreApplication.translate("starterDialog", u"Back", None))
        self.label_2.setText(QCoreApplication.translate("starterDialog", u"New Passowrd", None))
        self.new_password_input.setPlaceholderText(QCoreApplication.translate("starterDialog", u"password", None))
        self.confirm_password_input.setPlaceholderText(QCoreApplication.translate("starterDialog", u"repeat password", None))
        self.label_7.setText(QCoreApplication.translate("starterDialog", u"New Passphrase", None))
        self.new_passphrase.setPlaceholderText(QCoreApplication.translate("starterDialog", u"passphrase", None))
        self.passphrasepage_next_btn.setText(QCoreApplication.translate("starterDialog", u"Next", None))
        self.label_8.setText(QCoreApplication.translate("starterDialog", u"Confirm Passphrase", None))
        self.confirm_passphrase.setPlaceholderText(QCoreApplication.translate("starterDialog", u"repeat passphrase", None))
        self.passphrasepage_back_btn.setText(QCoreApplication.translate("starterDialog", u"Back", None))
        self.generate_passphrase_btn.setText(QCoreApplication.translate("starterDialog", u"Generate", None))
        self.passphrase_backup.setText(QCoreApplication.translate("starterDialog", u"Backup with a secret phrasee", None))
        self.copy_recovery_phrase_btn.setText(QCoreApplication.translate("starterDialog", u"Copy", None))
        self.label_9.setText(QCoreApplication.translate("starterDialog", u"Secret  recovery phrase", None))
        self.label_10.setText(QCoreApplication.translate("starterDialog", u"Use this secret phrase to recover. Make sure you save it and ", None))
        self.label_11.setText(QCoreApplication.translate("starterDialog", u"and never share to anyone.", None))
        self.recovery_page_baxk.setText(QCoreApplication.translate("starterDialog", u"Back", None))
        self.recovery_page_next.setText(QCoreApplication.translate("starterDialog", u"Next", None))
        self.success_page_next.setText(QCoreApplication.translate("starterDialog", u"Next", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("starterDialog", u"Welcome to LockBox", None))
    # retranslateUi

