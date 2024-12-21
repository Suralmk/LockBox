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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)
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
"border-bottom: 1px solid rgba(102,102,102,0.3);\n"
"background: rgba(20, 24, 21, 0.3) ;\n"
"\n"
"}\n"
"QPushButton {\n"
"background: transparent;\n"
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
        icon.addFile(u":/icons/icons/subtract-line.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon1.addFile(u":/icons/icons/close-large-line.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
"padding-left: 15px;\n"
"background: transparent;\n"
"")

        self.gridLayout_8.addWidget(self.label_12, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(599, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.title_bar, 0, 0, 1, 1)

        self.stack_1 = QStackedWidget(self.centralwidget)
        self.stack_1.setObjectName(u"stack_1")
        self.stack_1.setStyleSheet(u"QPushButton {\n"
"		text-align:center;\n"
"color:rgba(240, 247, 255,0.7);\n"
"         font-size:15px;\n"
"padding: 7px 10px;\n"
"border:none;\n"
"border-radius:5px;\n"
"background-color: rgba(32,144,46,1);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(32,144,46,0.8);\n"
"}\n"
"\n"
"QLineEdit {\n"
"border-radius:5px;\n"
"border: 1px solid rgba(102,102,102,1);\n"
"background: rgba(35,39,42,1);\n"
"padding-left: 15px;\n"
"color: white;\n"
"}")
        self.landingpage = QWidget()
        self.landingpage.setObjectName(u"landingpage")
        self.label_7 = QLabel(self.landingpage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 150, 201, 41))
        self.label_7.setStyleSheet(u"font: 20pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"padding-left: 15px;\n"
"text-align:center;")
        self.landingpage_get_started_btn = QPushButton(self.landingpage)
        self.landingpage_get_started_btn.setObjectName(u"landingpage_get_started_btn")
        self.landingpage_get_started_btn.setGeometry(QRect(300, 250, 261, 35))
        self.landingpage_get_started_btn.setMinimumSize(QSize(0, 35))
        self.landingpage_get_started_btn.setMaximumSize(QSize(16777215, 30))
        self.landingpage_get_started_btn.setStyleSheet(u"")
        self.landingpage_get_started_btn.setCheckable(True)
        self.landingpage_get_started_btn.setAutoExclusive(True)
        self.stack_1.addWidget(self.landingpage)
        self.loginpage = QWidget()
        self.loginpage.setObjectName(u"loginpage")
        self.label_4 = QLabel(self.loginpage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 119, 121, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setStyleSheet(u"font: 20pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"padding-left: 15px;\n"
"text-align:center;")
        self.layoutWidget = QWidget(self.loginpage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(261, 171, 381, 191))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgb(240, 247, 255);\n"
"background:transparent;\n"
"")

        self.verticalLayout.addWidget(self.label_3)

        self.stack_1_password_input = QLineEdit(self.layoutWidget)
        self.stack_1_password_input.setObjectName(u"stack_1_password_input")
        self.stack_1_password_input.setMinimumSize(QSize(30, 35))
        self.stack_1_password_input.setMaximumSize(QSize(16777215, 30))
        self.stack_1_password_input.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.stack_1_password_input)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stack_1_login_btn = QPushButton(self.layoutWidget)
        self.stack_1_login_btn.setObjectName(u"stack_1_login_btn")
        self.stack_1_login_btn.setMinimumSize(QSize(0, 35))
        self.stack_1_login_btn.setMaximumSize(QSize(16777215, 30))
        self.stack_1_login_btn.setStyleSheet(u"")
        self.stack_1_login_btn.setCheckable(True)
        self.stack_1_login_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.stack_1_login_btn)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"\n"
"QPushButton {\n"
"padding:0;\n"
"background:transparent;\n"
"padding: 0 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color:white;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

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
        icon3.addFile(u":/icons/icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon4.addFile(u":/icons/icons/lock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.encryptpage_btn.setIcon(icon4)
        self.encryptpage_btn.setCheckable(True)
        self.encryptpage_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.encryptpage_btn)

        self.dcryptpage_btn = QPushButton(self.layoutWidget_4)
        self.dcryptpage_btn.setObjectName(u"dcryptpage_btn")
        self.dcryptpage_btn.setMaximumSize(QSize(16777215, 40))
        self.dcryptpage_btn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/unlock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dcryptpage_btn.setIcon(icon5)
        self.dcryptpage_btn.setCheckable(True)
        self.dcryptpage_btn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dcryptpage_btn)

        self.helppage_btn = QPushButton(self.layoutWidget_4)
        self.helppage_btn.setObjectName(u"helppage_btn")
        self.helppage_btn.setMaximumSize(QSize(16777215, 40))
        self.helppage_btn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/settings-3-line.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"\n"
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
"\n"
"border: 1px solid rgba(102,102,102,1);\n"
"background: rgba(35,39,42,1);\n"
"padding-left: 15px;\n"
"color: white;\n"
"border-radius:px;\n"
"}\n"
"\n"
"    QTextEdit QScrollBar:vertical {\n"
"        width: 10px; /* Decrease the width of the scrollbar */\n"
"        background:  rgba(35,39,42,1); /* Set the background color to black */\n"
"    }\n"
"    QTextEdit QScrollBar:handle:vertical {\n"
"        background: rgba(102,102,102,1); /* Handle color - dark gray */\n"
"        border-radius: 5px; /* Option"
                        "al rounded corners */\n"
"    }\n"
"    QTextEdit QScrollBar:add-line:vertical, QTextEdit QScrollBar:sub-line:vertical {\n"
"        border: none; /* Hide the add/sub buttons */\n"
"    }\n"
"    QTextEdit QScrollBar:up-arrow:vertical, QTextEdit QScrollBar:down-arrow:vertical {\n"
"        border: none;\n"
"        background: none;\n"
"    }\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border: 1px solid white ;\n"
"    border-radius: 4px;\n"
"background: rgba(35,39,42,1);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid white;\n"
"background-color: rgba(32,144,46,1);\n"
"}\n"
"\n"
"QCheckBox {\n"
"    spacing: 10px;\n"
"    font-size: 14px;\n"
"    color: black;\n"
"}\n"
"\n"
"")
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
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 70))
        self.label_14.setMaximumSize(QSize(16777215, 70))
        self.label_14.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255, 1);\n"
"background:transparent;\n"
"font-weight:bold;")

        self.verticalLayout_7.addWidget(self.label_14)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(28)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(25)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 130))
        self.frame_5.setMaximumSize(QSize(200, 130))
        self.frame_5.setStyleSheet(u"background-color: rgba(32,144,46,0.5);\n"
"")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(71, 21, 102, 27))
        self.label_19.setStyleSheet(u"border-radius:0px;\n"
"background:transparent;\n"
"font: 12pt \"Segoe UI\";\n"
"font-weight:bold;\n"
"background:none;")
        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 80, 141, 41))
        self.label_25.setStyleSheet(u"border-radius:0px;\n"
"background:transparent;\n"
"font: 20pt \"Segoe UI\";\n"
"font-weight:bold;\n"
"color:white;")
        self.label_22 = QLabel(self.frame_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(70, 50, 42, 27))
        self.label_22.setStyleSheet(u"border-radius:0px;\n"
"background:transparent;\n"
"font: 12pt \"Segoe UI\";\n"
"font-weight:bold;")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 30, 31, 31))
        self.label_8.setStyleSheet(u"background:none;")
        self.label_8.setPixmap(QPixmap(u":/icons/icons/key-2-line.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(200, 130))
        self.frame_6.setMaximumSize(QSize(200, 130))
        self.frame_6.setStyleSheet(u"background: #141815;")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(81, 21, 102, 27))
        self.label_23.setStyleSheet(u"border-radius:0px;\n"
"background:transparent;\n"
"font: 12pt \"Segoe UI\";\n"
"font-weight:bold;\n"
"background:none;")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 30, 31, 31))
        self.label_9.setStyleSheet(u"background:none;")
        self.label_9.setPixmap(QPixmap(u":/icons/icons/lock-unlock-line.png"))
        self.label_9.setScaledContents(True)
        self.label_27 = QLabel(self.frame_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(80, 50, 42, 27))
        self.label_27.setStyleSheet(u"border-radius:0px;\n"
"background:transparent;\n"
"font: 12pt \"Segoe UI\";\n"
"font-weight:bold;")
        self.label_28 = QLabel(self.frame_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 80, 151, 41))
        self.label_28.setStyleSheet(u"border-radius:0px;\n"
"background:transparent;\n"
"font: 20pt \"Segoe UI\";\n"
"font-weight:bold;\n"
"color:white;")

        self.horizontalLayout_7.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(200, 130))
        self.frame_7.setMaximumSize(QSize(200, 130))
        self.frame_7.setStyleSheet(u"background:#616961;")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 10, 121, 31))
        self.label_29.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,1);\n"
"background:transparent;\n"
"font-weight:bold;")
        self.label_31 = QLabel(self.frame_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 70, 141, 41))
        self.label_31.setStyleSheet(u"border-radius:0px;\n"
"background:transparent;\n"
"font: 20pt \"Segoe UI\";\n"
"font-weight:bold;\n"
"color:white;")

        self.horizontalLayout_7.addWidget(self.frame_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setMaximumSize(QSize(16777215, 70))
        self.label_15.setStyleSheet(u"border-radius:0px;\n"
"background:transparent;\n"
"font: 12pt \"Segoe UI\";\n"
"font-weight:bold;\n"
"background:none;")

        self.verticalLayout_5.addWidget(self.label_15)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.frame)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.gridLayout_7.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.label_30 = QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"border-radius:0px;\n"
"background:transparent;\n"
"font: 12pt \"Segoe UI\";\n"
"font-weight:bold;\n"
"background:none;")

        self.gridLayout_7.addWidget(self.label_30, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_9.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stack_2.addWidget(self.homepage)
        self.settingspage = QWidget()
        self.settingspage.setObjectName(u"settingspage")
        self.save_settings_btn = QPushButton(self.settingspage)
        self.save_settings_btn.setObjectName(u"save_settings_btn")
        self.save_settings_btn.setGeometry(QRect(550, 480, 120, 35))
        self.save_settings_btn.setMinimumSize(QSize(0, 35))
        self.save_settings_btn.setMaximumSize(QSize(120, 35))
        self.save_settings_btn.setStyleSheet(u"QPushButton {\n"
"		text-align:center;\n"
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
        self.save_settings_btn.setCheckable(True)
        self.save_settings_btn.setAutoExclusive(True)
        self.label_20 = QLabel(self.settingspage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 10, 621, 70))
        self.label_20.setMinimumSize(QSize(0, 70))
        self.label_20.setMaximumSize(QSize(16777215, 70))
        self.label_20.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255, 1);\n"
"background:transparent;\n"
"font-weight:bold;")
        self.layoutWidget1 = QWidget(self.settingspage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 190, 211, 23))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.auto_delete_checkbox = QCheckBox(self.layoutWidget1)
        self.auto_delete_checkbox.setObjectName(u"auto_delete_checkbox")
        self.auto_delete_checkbox.setMinimumSize(QSize(20, 20))
        self.auto_delete_checkbox.setMaximumSize(QSize(20, 20))
        self.auto_delete_checkbox.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.auto_delete_checkbox)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.layoutWidget_2 = QWidget(self.settingspage)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 280, 341, 36))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.change_passphrase_btn = QPushButton(self.layoutWidget_2)
        self.change_passphrase_btn.setObjectName(u"change_passphrase_btn")
        self.change_passphrase_btn.setMaximumSize(QSize(16777215, 40))
        self.change_passphrase_btn.setMouseTracking(True)
        self.change_passphrase_btn.setStyleSheet(u"QPushButton {\n"
"		text-align:center;\n"
"color:rgba(240, 247, 255,0.7);\n"
"         font-size:15px;\n"
"		padding-left: 15px;\n"
"padding: 7px 10px;\n"
"border:none;\n"
"background-color: rgba(55, 61, 56, 1);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(240, 247, 255,0.1);\n"
"}")
        self.change_passphrase_btn.setCheckable(True)
        self.change_passphrase_btn.setChecked(True)
        self.change_passphrase_btn.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.change_passphrase_btn)

        self.layoutWidget2 = QWidget(self.settingspage)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(14, 80, 571, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.change_location_btn = QPushButton(self.layoutWidget2)
        self.change_location_btn.setObjectName(u"change_location_btn")
        self.change_location_btn.setMaximumSize(QSize(16777215, 40))
        self.change_location_btn.setMouseTracking(True)
        self.change_location_btn.setStyleSheet(u"QPushButton {\n"
"		text-align:center;\n"
"color:rgba(240, 247, 255,0.7);\n"
"         font-size:15px;\n"
"		padding-left: 15px;\n"
"padding: 7px 10px;\n"
"border:none;\n"
"background-color: rgba(55, 61, 56, 1);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(240, 247, 255,0.1);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/folder-3-fill.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.change_location_btn.setIcon(icon7)
        self.change_location_btn.setCheckable(True)
        self.change_location_btn.setChecked(True)
        self.change_location_btn.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.change_location_btn)

        self.setting_location_input = QLineEdit(self.layoutWidget2)
        self.setting_location_input.setObjectName(u"setting_location_input")
        self.setting_location_input.setMinimumSize(QSize(30, 35))
        self.setting_location_input.setMaximumSize(QSize(16777215, 30))
        self.setting_location_input.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.setting_location_input)

        self.layoutWidget3 = QWidget(self.settingspage)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 150, 316, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hide_encrypted_files_checkbox = QCheckBox(self.layoutWidget3)
        self.hide_encrypted_files_checkbox.setObjectName(u"hide_encrypted_files_checkbox")
        self.hide_encrypted_files_checkbox.setMinimumSize(QSize(20, 20))
        self.hide_encrypted_files_checkbox.setMaximumSize(QSize(20, 20))
        self.hide_encrypted_files_checkbox.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.hide_encrypted_files_checkbox)

        self.label = QLabel(self.layoutWidget3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.layoutWidget4 = QWidget(self.settingspage)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 230, 341, 36))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.change_password_btn = QPushButton(self.layoutWidget4)
        self.change_password_btn.setObjectName(u"change_password_btn")
        self.change_password_btn.setMaximumSize(QSize(16777215, 40))
        self.change_password_btn.setMouseTracking(True)
        self.change_password_btn.setStyleSheet(u"QPushButton {\n"
"		text-align:center;\n"
"color:rgba(240, 247, 255,0.7);\n"
"         font-size:15px;\n"
"		padding-left: 15px;\n"
"padding: 7px 10px;\n"
"border:none;\n"
"background-color: rgba(55, 61, 56, 1);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(240, 247, 255,0.1);\n"
"}")
        self.change_password_btn.setCheckable(True)
        self.change_password_btn.setChecked(True)
        self.change_password_btn.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.change_password_btn)

        self.stack_2.addWidget(self.settingspage)
        self.dcryptpage = QWidget()
        self.dcryptpage.setObjectName(u"dcryptpage")
        self.gridLayout_14 = QGridLayout(self.dcryptpage)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_24 = QLabel(self.dcryptpage)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 70))
        self.label_24.setMaximumSize(QSize(16777215, 70))
        self.label_24.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color:rgb(240, 247, 255);\n"
"background:transparent;\n"
"font-weight:bold;")

        self.gridLayout_14.addWidget(self.label_24, 0, 0, 1, 1)

        self.encrypt_file_upload_progress_bar_2 = QFrame(self.dcryptpage)
        self.encrypt_file_upload_progress_bar_2.setObjectName(u"encrypt_file_upload_progress_bar_2")
        self.encrypt_file_upload_progress_bar_2.setMinimumSize(QSize(0, 300))
        self.encrypt_file_upload_progress_bar_2.setStyleSheet(u"QPushButton {\n"
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
        self.encrypt_file_upload_progress_bar_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.encrypt_file_upload_progress_bar_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.encrypt_file_upload_progress_bar_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(0)
        self.gridLayout_10.setVerticalSpacing(5)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.encrypt_file_upload_progress_bar_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_10)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame {\n"
"background: rgba(0,0,0,0.1);\n"
"border: 2px dashed rgba(102, 102, 102, 1);\n"
"\n"
"}")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_11)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.dcrypt_select_file_2 = QPushButton(self.frame_11)
        self.dcrypt_select_file_2.setObjectName(u"dcrypt_select_file_2")
        self.dcrypt_select_file_2.setMinimumSize(QSize(135, 0))
        self.dcrypt_select_file_2.setMaximumSize(QSize(135, 40))
        self.dcrypt_select_file_2.setStyleSheet(u"border-radius:5px;")
        self.dcrypt_select_file_2.setCheckable(True)
        self.dcrypt_select_file_2.setAutoExclusive(True)

        self.gridLayout_13.addWidget(self.dcrypt_select_file_2, 1, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_11, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_10, 2, 0, 1, 1)

        self.progressBar_2 = QProgressBar(self.encrypt_file_upload_progress_bar_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)

        self.gridLayout_10.addWidget(self.progressBar_2, 1, 0, 1, 1)


        self.gridLayout_14.addWidget(self.encrypt_file_upload_progress_bar_2, 1, 0, 1, 1)

        self.dcrypt_logs_2 = QTextEdit(self.dcryptpage)
        self.dcrypt_logs_2.setObjectName(u"dcrypt_logs_2")
        self.dcrypt_logs_2.setMaximumSize(QSize(682, 187))
        self.dcrypt_logs_2.setStyleSheet(u"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"color:rgba(255, 255, 255, 0.8);\n"
"font: 11pt \"Segoe UI\";")

        self.gridLayout_14.addWidget(self.dcrypt_logs_2, 2, 0, 1, 1)

        self.stack_2.addWidget(self.dcryptpage)
        self.encryptpage = QWidget()
        self.encryptpage.setObjectName(u"encryptpage")
        self.gridLayout_3 = QGridLayout(self.encryptpage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.dcrypt_logs = QTextEdit(self.encryptpage)
        self.dcrypt_logs.setObjectName(u"dcrypt_logs")
        self.dcrypt_logs.setMaximumSize(QSize(682, 187))
        self.dcrypt_logs.setStyleSheet(u"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"color:rgba(255, 255, 255, 0.8);\n"
"font: 11pt \"Segoe UI\";")

        self.gridLayout_3.addWidget(self.dcrypt_logs, 3, 0, 1, 2)

        self.encrypt_file_upload_progress_bar = QFrame(self.encryptpage)
        self.encrypt_file_upload_progress_bar.setObjectName(u"encrypt_file_upload_progress_bar")
        self.encrypt_file_upload_progress_bar.setMinimumSize(QSize(0, 300))
        self.encrypt_file_upload_progress_bar.setStyleSheet(u"QPushButton {\n"
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
        self.encrypt_file_upload_progress_bar.setFrameShape(QFrame.Shape.StyledPanel)
        self.encrypt_file_upload_progress_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.encrypt_file_upload_progress_bar)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.encrypt_file_upload_progress_bar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_4.addWidget(self.progressBar, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.encrypt_file_upload_progress_bar)
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

        self.gridLayout_6.addWidget(self.dcrypt_select_file, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.encrypt_file_upload_progress_bar, 1, 0, 1, 2)

        self.label_21 = QLabel(self.encryptpage)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 70))
        self.label_21.setMaximumSize(QSize(16777215, 70))
        self.label_21.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color:rgb(240, 247, 255);\n"
"background:transparent;\n"
"font-weight:bold;")

        self.gridLayout_3.addWidget(self.label_21, 0, 0, 1, 2)

        self.stack_2.addWidget(self.encryptpage)

        self.gridLayout_2.addWidget(self.stack_2, 0, 1, 1, 1)

        self.stack_1.addWidget(self.mainpage)

        self.gridLayout.addWidget(self.stack_1, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.minimize_btn.clicked.connect(MainWindow.showMinimized)
        self.close_btn.clicked.connect(MainWindow.close)

        self.stack_1.setCurrentIndex(2)
        self.stack_2.setCurrentIndex(0)


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
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Landing Page", None))
        self.landingpage_get_started_btn.setText(QCoreApplication.translate("MainWindow", u"Get Started", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"LockBox", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Input Password", None))
        self.stack_1_password_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.stack_1_login_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Forgot Password", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Powered by Surafel Production", None))
        self.visit_website_btn.setText(QCoreApplication.translate("MainWindow", u"Visit website", None))
        self.homepage_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.encryptpage_btn.setText(QCoreApplication.translate("MainWindow", u"Encrypt Files", None))
        self.dcryptpage_btn.setText(QCoreApplication.translate("MainWindow", u"Dcrypt Files", None))
        self.helppage_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"   Dashboard", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Encrypted ", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.label_8.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Decrypted", None))
        self.label_9.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"File Type", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"   Recent Activity", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"   Encrypt Images, Audio, Video, Documents, Folders and Files.", None))
        self.save_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.auto_delete_checkbox.setText(QCoreApplication.translate("MainWindow", u"dsdsffsd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Auto delete original file", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Change Passphrase", None))
        self.change_passphrase_btn.setText(QCoreApplication.translate("MainWindow", u"Change Passphrase", None))
        self.change_location_btn.setText(QCoreApplication.translate("MainWindow", u"Change Location", None))
        self.setting_location_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.hide_encrypted_files_checkbox.setText(QCoreApplication.translate("MainWindow", u"dsdsffsd", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hide encrypted files from the file system", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Create a new password", None))
        self.change_password_btn.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Decrypt Files", None))
        self.dcrypt_select_file_2.setText(QCoreApplication.translate("MainWindow", u"Slelect File", None))
        self.dcrypt_select_file.setText(QCoreApplication.translate("MainWindow", u"Slelect File", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Encrypt Files", None))
    # retranslateUi

