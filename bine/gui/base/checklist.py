# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'checklist.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QListWidget,
    QListWidgetItem, QSizePolicy, QStackedWidget, QWidget)

class Ui_ChecklistWidget(object):
    def setupUi(self, ChecklistWidget):
        if not ChecklistWidget.objectName():
            ChecklistWidget.setObjectName(u"ChecklistWidget")
        ChecklistWidget.resize(622, 360)
        self.horizontalLayout = QHBoxLayout(ChecklistWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.items = QListWidget(ChecklistWidget)
        self.items.setObjectName(u"items")
        self.items.setDragDropMode(QAbstractItemView.InternalMove)
        self.items.setDefaultDropAction(Qt.MoveAction)
        self.items.setAlternatingRowColors(True)

        self.horizontalLayout.addWidget(self.items)

        self.children = QStackedWidget(ChecklistWidget)
        self.children.setObjectName(u"children")

        self.horizontalLayout.addWidget(self.children)


        self.retranslateUi(ChecklistWidget)

        QMetaObject.connectSlotsByName(ChecklistWidget)
    # setupUi

    def retranslateUi(self, ChecklistWidget):
        ChecklistWidget.setWindowTitle(QCoreApplication.translate("ChecklistWidget", u"Form", None))
    # retranslateUi

