# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MessageBox.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import resources_rc

class Ui_MessageBox(object):
    def setupUi(self, MessageBox):
        if not MessageBox.objectName():
            MessageBox.setObjectName(u"MessageBox")
        MessageBox.resize(400, 180)
        MessageBox.setMinimumSize(QSize(400, 180))
        MessageBox.setMaximumSize(QSize(409, 180))
        MessageBox.setStyleSheet(u"\n"
"QDialog {\n"
"background:  rgba(35,39,42,1);\n"
"border-radius: 15px;\n"
"\n"
"}\n"
"QPushButton {\n"
"		text-align:center;\n"
"color:rgba(240, 247, 255,0.7);\n"
"         font-size:14px;\n"
"		padding-left: 15px;\n"
"padding: 7px 10px;\n"
"border:none;\n"
"background-color: rgba(55, 61, 56, 1);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(240, 247, 255,0.1);\n"
"}\n"
"\n"
" QLabel {\n"
"                font-size: 14px;\n"
"                color: #333;\n"
"                padding-left: 15px;\n"
"            }")
        self.gridLayout = QGridLayout(MessageBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.title_bar = QWidget(MessageBox)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(400, 40))
        self.title_bar.setMaximumSize(QSize(300, 40))
        self.title_bar.setStyleSheet(u"QWidget {\n"
"border: none;\n"
"padding: none;\n"
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
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.close_btn = QPushButton(self.title_bar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(45, 39))
        self.close_btn.setMaximumSize(QSize(40, 39))
        self.close_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/close-large-line.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(15, 15))

        self.gridLayout_2.addWidget(self.close_btn, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(599, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.title_bar, 0, 0, 1, 1)

        self.message_text = QLabel(MessageBox)
        self.message_text.setObjectName(u"message_text")
        self.message_text.setMinimumSize(QSize(390, 70))
        self.message_text.setMaximumSize(QSize(390, 154245))
        self.message_text.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgba(240, 247, 255,0.7);\n"
"background:transparent;\n"
"")
        self.message_text.setWordWrap(True)

        self.gridLayout.addWidget(self.message_text, 1, 0, 1, 1)

        self.frame = QFrame(MessageBox)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 10, -1)
        self.message_cancel_btn = QPushButton(self.frame)
        self.message_cancel_btn.setObjectName(u"message_cancel_btn")
        self.message_cancel_btn.setMinimumSize(QSize(90, 30))
        self.message_cancel_btn.setMaximumSize(QSize(90, 30))
        self.message_cancel_btn.setMouseTracking(True)
        self.message_cancel_btn.setStyleSheet(u"")
        self.message_cancel_btn.setCheckable(True)
        self.message_cancel_btn.setChecked(True)
        self.message_cancel_btn.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.message_cancel_btn)

        self.message_continue_btn = QPushButton(self.frame)
        self.message_continue_btn.setObjectName(u"message_continue_btn")
        self.message_continue_btn.setMinimumSize(QSize(90, 30))
        self.message_continue_btn.setMaximumSize(QSize(90, 30))
        self.message_continue_btn.setMouseTracking(True)
        self.message_continue_btn.setStyleSheet(u"")
        self.message_continue_btn.setCheckable(True)
        self.message_continue_btn.setChecked(True)
        self.message_continue_btn.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.message_continue_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(MessageBox)
        self.close_btn.clicked.connect(MessageBox.close)

        QMetaObject.connectSlotsByName(MessageBox)
    # setupUi

    def retranslateUi(self, MessageBox):
        MessageBox.setWindowTitle(QCoreApplication.translate("MessageBox", u"Dialog", None))
        self.close_btn.setText("")
        self.message_text.setText(QCoreApplication.translate("MessageBox", u"--", None))
        self.message_cancel_btn.setText(QCoreApplication.translate("MessageBox", u"Cancel", None))
        self.message_continue_btn.setText(QCoreApplication.translate("MessageBox", u"Continue", None))
    # retranslateUi

