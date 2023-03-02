# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QColumnView, QGroupBox, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

from bine.gui.widgets.editor import MarkdownSpellTextEdit

class Ui_Tab(object):
    def setupUi(self, Tab):
        if not Tab.objectName():
            Tab.setObjectName(u"Tab")
        Tab.resize(813, 531)
        self.verticalLayout_2 = QVBoxLayout(Tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.group = QGroupBox(Tab)
        self.group.setObjectName(u"group")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.group.sizePolicy().hasHeightForWidth())
        self.group.setSizePolicy(sizePolicy)
        self.group.setFlat(True)
        self.group.setCheckable(True)
        self.verticalLayout = QVBoxLayout(self.group)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 6, 0, 0)
        self.title = QLineEdit(self.group)
        self.title.setObjectName(u"title")

        self.verticalLayout.addWidget(self.title)

        self.description = MarkdownSpellTextEdit(self.group)
        self.description.setObjectName(u"description")
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(10)
        self.description.setFont(font)

        self.verticalLayout.addWidget(self.description)


        self.verticalLayout_2.addWidget(self.group)

        self.columns = QColumnView(Tab)
        self.columns.setObjectName(u"columns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.columns.sizePolicy().hasHeightForWidth())
        self.columns.setSizePolicy(sizePolicy1)
        self.columns.setDragEnabled(True)

        self.verticalLayout_2.addWidget(self.columns)


        self.retranslateUi(Tab)

        QMetaObject.connectSlotsByName(Tab)
    # setupUi

    def retranslateUi(self, Tab):
        Tab.setWindowTitle(QCoreApplication.translate("Tab", u"Form", None))
        self.group.setTitle(QCoreApplication.translate("Tab", u"Document Details:", None))
        self.title.setPlaceholderText(QCoreApplication.translate("Tab", u"Document Title...", None))
        self.description.setPlaceholderText(QCoreApplication.translate("Tab", u"Document description...", None))
    # retranslateUi

