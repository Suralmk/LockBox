# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 585)
        MainWindow.setMinimumSize(QSize(900, 585))
        MainWindow.setMaximumSize(QSize(900, 585))
        MainWindow.setStyleSheet(u"background:#23272a;")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionFiles = QAction(MainWindow)
        self.actionFiles.setObjectName(u"actionFiles")
        self.actionFolders = QAction(MainWindow)
        self.actionFolders.setObjectName(u"actionFolders")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionImages = QAction(MainWindow)
        self.actionImages.setObjectName(u"actionImages")
        self.actionViedos = QAction(MainWindow)
        self.actionViedos.setObjectName(u"actionViedos")
        self.actionOther = QAction(MainWindow)
        self.actionOther.setObjectName(u"actionOther")
        self.actionGet_Key = QAction(MainWindow)
        self.actionGet_Key.setObjectName(u"actionGet_Key")
        self.actionNew_Key = QAction(MainWindow)
        self.actionNew_Key.setObjectName(u"actionNew_Key")
        self.actionGet_Help = QAction(MainWindow)
        self.actionGet_Help.setObjectName(u"actionGet_Help")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QWidget(self.centralwidget)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(900, 40))
        self.title_bar.setMaximumSize(QSize(16777215, 40))
        self.title_bar.setStyleSheet(u"QWidget {\n"
"border-bottom: 1px solid rgba(102,102,102,0.5);\n"
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
"\n"
"}")
        self.gridLayout_8 = QGridLayout(self.title_bar)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minimize_btn = QPushButton(self.title_bar)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(45, 3))
        self.minimize_btn.setMaximumSize(QSize(40, 39))
        self.minimize_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/src/icons/subtract-line.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(self.title_bar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(45, 39))
        self.close_btn.setMaximumSize(QSize(40, 39))
        self.close_btn.setStyleSheet(u"QPushButton:hover {\n"
"background:   rgba(227,25,25,1);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/src/icons/close-large-line.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon1)
        self.close_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout.addWidget(self.close_btn)


        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 2, 1, 1)

        self.label_12 = QLabel(self.title_bar)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(200, 0))
        self.label_12.setMaximumSize(QSize(16777215, 40))
        self.label_12.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background: #141815;\n"
"padding-left: 15px;")

        self.gridLayout_8.addWidget(self.label_12, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(599, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.title_bar, 0, 0, 1, 1)

        self.stack_1 = QStackedWidget(self.centralwidget)
        self.stack_1.setObjectName(u"stack_1")
        self.stack_1.setStyleSheet(u"background:#23272a;")
        self.loginpage = QWidget()
        self.loginpage.setObjectName(u"loginpage")
        self.widget_2 = QWidget(self.loginpage)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(220, 40, 451, 321))
        self.widget_2.setStyleSheet(u"\n"
"QWidget {\n"
"background:white;\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"background:rgb(14, 59, 98);\n"
"color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background:rgba(14, 59, 98, 0.8);\n"
"}\n"
"\n"
"QLineEdit {\n"
"}")
        self.pushButton_14 = QPushButton(self.widget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(140, 260, 179, 35))
        self.pushButton_14.setMinimumSize(QSize(0, 35))
        self.pushButton_14.setMaximumSize(QSize(16777215, 30))
        self.pushButton_14.setStyleSheet(u"")
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setAutoExclusive(True)
        self.layoutWidget_2 = QWidget(self.widget_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 100, 391, 131))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(70, 30))
        self.lineEdit_4.setStyleSheet(u"background:white;\n"
"padding-left:10px;\n"
"")

        self.verticalLayout_3.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(70, 30))
        self.lineEdit_5.setStyleSheet(u"background:white;\n"
"padding-left:10px;")

        self.verticalLayout_3.addWidget(self.lineEdit_5)

        self.lineEdit_8 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(70, 30))
        self.lineEdit_8.setStyleSheet(u"background:white;\n"
"padding-left:10px;")

        self.verticalLayout_3.addWidget(self.lineEdit_8)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(90, 40, 291, 31))
        self.label_11.setStyleSheet(u"font: 300 16pt \"Segoe UI\";")
        self.stack_1.addWidget(self.loginpage)
        self.mainpage = QWidget()
        self.mainpage.setObjectName(u"mainpage")
        self.gridLayout_2 = QGridLayout(self.mainpage)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.mainpage)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(200, 550))
        self.widget_4.setStyleSheet(u"QWidget {\n"
"background: #141815;\n"
"}\n"
"QPushButton {\n"
"		text-align:left;\n"
"color:rgba(240, 247, 255,0.7);\n"
"         font-size:15px;\n"
"		padding-left: 15px;\n"
"padding: 7px 10px;\n"
"border:none\n"
"}\n"
"QPushButton:checked {\n"
"background-color: rgba(32,144,46,1);\n"
"border-radius:5px;\n"
"color:rgba(240, 247, 255, 1);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgba(240, 247, 255,0.1);\n"
"}")
        self.label_13 = QLabel(self.widget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 510, 181, 31))
        self.label_13.setStyleSheet(u"color:rgba(240, 247, 255,0.5);")
        self.visit_website_btn = QPushButton(self.widget_4)
        self.visit_website_btn.setObjectName(u"visit_website_btn")
        self.visit_website_btn.setGeometry(QRect(10, 480, 179, 31))
        self.visit_website_btn.setMaximumSize(QSize(16777215, 40))
        self.visit_website_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/src/icons/links-line.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.visit_website_btn.setIcon(icon2)
        self.visit_website_btn.setCheckable(False)
        self.visit_website_btn.setAutoExclusive(True)
        self.layoutWidget_4 = QWidget(self.widget_4)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 100, 181, 156))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.homepage_btn = QPushButton(self.layoutWidget_4)
        self.homepage_btn.setObjectName(u"homepage_btn")
        self.homepage_btn.setMaximumSize(QSize(16777215, 40))
        self.homepage_btn.setMouseTracking(True)
        self.homepage_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/src/icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homepage_btn.setIcon(icon3)
        self.homepage_btn.setCheckable(True)
        self.homepage_btn.setChecked(True)
        self.homepage_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.homepage_btn)

        self.encryptpage_btn = QPushButton(self.layoutWidget_4)
        self.encryptpage_btn.setObjectName(u"encryptpage_btn")
        self.encryptpage_btn.setMaximumSize(QSize(16777215, 40))
        self.encryptpage_btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/src/icons/lock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.encryptpage_btn.setIcon(icon4)
        self.encryptpage_btn.setCheckable(True)
        self.encryptpage_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.encryptpage_btn)

        self.dcryptpage_btn = QPushButton(self.layoutWidget_4)
        self.dcryptpage_btn.setObjectName(u"dcryptpage_btn")
        self.dcryptpage_btn.setMaximumSize(QSize(16777215, 40))
        self.dcryptpage_btn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/src/icons/unlock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dcryptpage_btn.setIcon(icon5)
        self.dcryptpage_btn.setCheckable(True)
        self.dcryptpage_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dcryptpage_btn)

        self.helppage_btn = QPushButton(self.layoutWidget_4)
        self.helppage_btn.setObjectName(u"helppage_btn")
        self.helppage_btn.setMaximumSize(QSize(16777215, 40))
        self.helppage_btn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/src/icons/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helppage_btn.setIcon(icon6)
        self.helppage_btn.setCheckable(True)
        self.helppage_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.helppage_btn)


        self.gridLayout_2.addWidget(self.widget_4, 0, 0, 1, 1)

        self.stack_2 = QStackedWidget(self.mainpage)
        self.stack_2.setObjectName(u"stack_2")
        self.stack_2.setMaximumSize(QSize(700, 550))
        self.stack_2.setStyleSheet(u"\n"
"\n"
"QStackedWidget {\n"
"background: rgba(35,39,42,1);\n"
"\n"
"}\n"
"\n"
"QWidget {\n"
"background: rgba(35,39,42,1);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QLabel {\n"
"background:transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"border-radius:5px;\n"
"border: 1px solid rgba(102,102,102,1);\n"
"background: rgba(35,39,42,1);\n"
"padding-left: 15px;\n"
"color: white;\n"
"}\n"
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
"        background: rgba(102,102,102,1); /* Handle color - dark gray */\n"
"        border-radius: 5px; /* Optional rounded corners */\n"
"    }\n"
"    QTextEdit QScrollBar:add-line:ver"
                        "tical, QTextEdit QScrollBar:sub-line:vertical {\n"
"        border: none; /* Hide the add/sub buttons */\n"
"    }\n"
"    QTextEdit QScrollBar:up-arrow:vertical, QTextEdit QScrollBar:down-arrow:vertical {\n"
"        border: none;\n"
"        background: none;\n"
"    }")
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.gridLayout_9 = QGridLayout(self.homepage)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.homepage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 700, 545))
        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 30, 351, 31))
        self.label_14.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,1);\n"
"background:transparent;")
        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(30, 120, 201, 131))
        self.frame_5.setStyleSheet(u"background-color: rgba(32,144,46,0.5);\n"
"")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 10, 121, 31))
        self.label_19.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,1);\n"
"background:transparent;\n"
"font-weight:bold;")
        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 50, 51, 21))
        self.label_25.setStyleSheet(u"border-radius:0px;\n"
"background:transparent;\n"
"font: 20pt \"Segoe UI\";\n"
"font-weight:bold;")
        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(30, 270, 661, 181))
        self.frame_8.setStyleSheet(u"background:white;")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.label_26 = QLabel(self.frame_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 20, 141, 21))
        self.label_26.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color:black;")
        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(260, 120, 201, 131))
        self.frame_6.setStyleSheet(u"background:rgba(69, 72, 208, 0.5)")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.label_27 = QLabel(self.frame_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 10, 121, 31))
        self.label_27.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,1);\n"
"background:transparent;\n"
"font-weight:bold;")
        self.label_28 = QLabel(self.frame_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 50, 51, 21))
        self.label_28.setStyleSheet(u"border-radius:0px;\n"
"background:transparent;\n"
"font: 18pt \"Segoe UI\";\n"
"font-weight:bold;")
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(490, 120, 201, 131))
        self.frame_7.setStyleSheet(u"background:rgba(189, 13, 1, 0.5)")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 10, 121, 31))
        self.label_29.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,1);\n"
"background:transparent;\n"
"font-weight:bold;")
        self.label_30 = QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(40, 470, 561, 31))
        self.label_30.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:black;\n"
"background:transparent;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_9.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stack_2.addWidget(self.homepage)
        self.helppage = QWidget()
        self.helppage.setObjectName(u"helppage")
        self.help_message_input = QTextEdit(self.helppage)
        self.help_message_input.setObjectName(u"help_message_input")
        self.help_message_input.setGeometry(QRect(10, 220, 500, 200))
        self.help_message_input.setStyleSheet(u"")
        self.help_send_btn = QPushButton(self.helppage)
        self.help_send_btn.setObjectName(u"help_send_btn")
        self.help_send_btn.setGeometry(QRect(10, 460, 179, 40))
        self.help_send_btn.setMinimumSize(QSize(0, 40))
        self.help_send_btn.setMaximumSize(QSize(16777215, 40))
        self.help_send_btn.setStyleSheet(u"QPushButton {\n"
"		text-align:left;\n"
"color:rgba(240, 247, 255,0.7);\n"
"         font-size:15px;\n"
"padding: 7px 10px;\n"
"border:none;\n"
"border-radius:5px;\n"
"background-color: rgba(32,144,46,1);\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgba(240, 247, 255,0.1);\n"
"}")
        self.help_send_btn.setCheckable(True)
        self.help_send_btn.setAutoExclusive(True)
        self.label_20 = QLabel(self.helppage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 10, 611, 31))
        self.label_20.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255, 1);\n"
"background:transparent;")
        self.halp_first_name_input = QLineEdit(self.helppage)
        self.halp_first_name_input.setObjectName(u"halp_first_name_input")
        self.halp_first_name_input.setGeometry(QRect(10, 120, 231, 30))
        self.halp_first_name_input.setMinimumSize(QSize(20, 0))
        self.halp_first_name_input.setStyleSheet(u"")
        self.help_phone_input = QLineEdit(self.helppage)
        self.help_phone_input.setObjectName(u"help_phone_input")
        self.help_phone_input.setGeometry(QRect(10, 170, 281, 30))
        self.help_phone_input.setMinimumSize(QSize(20, 0))
        self.help_phone_input.setStyleSheet(u"")
        self.stack_2.addWidget(self.helppage)
        self.dcryptpage = QWidget()
        self.dcryptpage.setObjectName(u"dcryptpage")
        self.encrypt_select_file = QPushButton(self.dcryptpage)
        self.encrypt_select_file.setObjectName(u"encrypt_select_file")
        self.encrypt_select_file.setGeometry(QRect(10, 500, 179, 30))
        self.encrypt_select_file.setMaximumSize(QSize(16777215, 40))
        self.encrypt_select_file.setStyleSheet(u"background:rgb(14, 59, 98);\n"
"color:white;\n"
"border-radius:5px;")
        self.encrypt_select_file.setCheckable(True)
        self.encrypt_select_file.setAutoExclusive(True)
        self.encrypt_start_btn = QPushButton(self.dcryptpage)
        self.encrypt_start_btn.setObjectName(u"encrypt_start_btn")
        self.encrypt_start_btn.setGeometry(QRect(500, 500, 179, 30))
        self.encrypt_start_btn.setMaximumSize(QSize(16777215, 40))
        self.encrypt_start_btn.setStyleSheet(u"background:rgb(14, 59, 98);\n"
"color:white;\n"
"border-radius:5px;")
        self.encrypt_start_btn.setCheckable(True)
        self.encrypt_start_btn.setAutoExclusive(True)
        self.label_24 = QLabel(self.dcryptpage)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 10, 311, 31))
        self.label_24.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color:rgb(240, 247, 255);\n"
"background:transparent;\n"
"font-weight:bold;")
        self.stack_2.addWidget(self.dcryptpage)
        self.encryptpage = QWidget()
        self.encryptpage.setObjectName(u"encryptpage")
        self.gridLayout_3 = QGridLayout(self.encryptpage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.dcrypt_logs = QTextEdit(self.encryptpage)
        self.dcrypt_logs.setObjectName(u"dcrypt_logs")
        self.dcrypt_logs.setStyleSheet(u"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"color:rgba(255, 255, 255, 0.8);\n"
"font: 11pt \"Segoe UI\";")

        self.gridLayout_3.addWidget(self.dcrypt_logs, 2, 0, 1, 2)

        self.frame = QFrame(self.encryptpage)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 300))
        self.frame.setStyleSheet(u"QPushButton {\n"
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
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(15)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.dcrypt_start_btn = QPushButton(self.frame_2)
        self.dcrypt_start_btn.setObjectName(u"dcrypt_start_btn")
        self.dcrypt_start_btn.setMinimumSize(QSize(120, 0))
        self.dcrypt_start_btn.setMaximumSize(QSize(120, 40))
        self.dcrypt_start_btn.setStyleSheet(u"border-radius:5px;")
        self.dcrypt_start_btn.setCheckable(True)
        self.dcrypt_start_btn.setAutoExclusive(True)

        self.gridLayout_7.addWidget(self.dcrypt_start_btn, 0, 0, 1, 1)

        self.homepage_btn_2 = QPushButton(self.frame_2)
        self.homepage_btn_2.setObjectName(u"homepage_btn_2")
        self.homepage_btn_2.setMinimumSize(QSize(120, 0))
        self.homepage_btn_2.setMaximumSize(QSize(120, 40))
        self.homepage_btn_2.setMouseTracking(True)
        self.homepage_btn_2.setStyleSheet(u"border-radius:5px;")
        self.homepage_btn_2.setIcon(icon3)
        self.homepage_btn_2.setCheckable(True)
        self.homepage_btn_2.setChecked(True)
        self.homepage_btn_2.setAutoExclusive(True)

        self.gridLayout_7.addWidget(self.homepage_btn_2, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame {\n"
"background: rgba(0,0,0,0.1);\n"
"border: 2px dashed rgba(102, 102, 102, 1);\n"
"\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.dcrypt_select_file = QPushButton(self.frame_4)
        self.dcrypt_select_file.setObjectName(u"dcrypt_select_file")
        self.dcrypt_select_file.setMinimumSize(QSize(135, 0))
        self.dcrypt_select_file.setMaximumSize(QSize(135, 40))
        self.dcrypt_select_file.setStyleSheet(u"border-radius:5px;")
        self.dcrypt_select_file.setCheckable(True)
        self.dcrypt_select_file.setAutoExclusive(True)

        self.gridLayout_6.addWidget(self.dcrypt_select_file, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 2)

        self.label_21 = QLabel(self.encryptpage)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color:rgb(240, 247, 255);\n"
"background:transparent;\n"
"font-weight:bold;")

        self.gridLayout_3.addWidget(self.label_21, 0, 0, 1, 1)

        self.stack_2.addWidget(self.encryptpage)

        self.gridLayout_2.addWidget(self.stack_2, 0, 1, 1, 1)

        self.stack_1.addWidget(self.mainpage)

        self.gridLayout.addWidget(self.stack_1, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.minimize_btn.clicked.connect(MainWindow.showMinimized)
        self.close_btn.clicked.connect(MainWindow.close)

        self.stack_1.setCurrentIndex(1)
        self.stack_2.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionFiles.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.actionFolders.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionImages.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.actionViedos.setText(QCoreApplication.translate("MainWindow", u"Folder", None))
        self.actionOther.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.actionGet_Key.setText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.actionNew_Key.setText(QCoreApplication.translate("MainWindow", u"New Key", None))
        self.actionGet_Help.setText(QCoreApplication.translate("MainWindow", u"Get Help", None))
        self.minimize_btn.setText("")
        self.close_btn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"LockBox", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Credentials for decrypting a file", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Powered by Surafel Production", None))
        self.visit_website_btn.setText(QCoreApplication.translate("MainWindow", u"Visit website", None))
        self.homepage_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.encryptpage_btn.setText(QCoreApplication.translate("MainWindow", u"Encrypt Files", None))
        self.dcryptpage_btn.setText(QCoreApplication.translate("MainWindow", u"Dcrypt Files", None))
        self.helppage_btn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Encrypt Files and Increase your safty", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Encrypted Files", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"How it works?", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"File Type", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"File Type", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Encrypt Images, Audio, Video, Documents, Folders and Files.", None))
        self.help_send_btn.setText(QCoreApplication.translate("MainWindow", u"Send Message", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Please Tell us the help you need and we will respond to you.", None))
        self.halp_first_name_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.help_phone_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.encrypt_select_file.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.encrypt_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Decrypt Files", None))
        self.dcrypt_start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.homepage_btn_2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.dcrypt_select_file.setText(QCoreApplication.translate("MainWindow", u"Slelect File", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Encrypt Files", None))
    # retranslateUi

