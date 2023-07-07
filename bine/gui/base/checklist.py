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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QListWidget,
    QListWidgetItem, QSizePolicy, QWidget)

class Ui_ChecklistWidget(object):
    def setupUi(self, ChecklistWidget):
        if not ChecklistWidget.objectName():
            ChecklistWidget.setObjectName(u"ChecklistWidget")
        ChecklistWidget.resize(400, 300)
        self.gridLayout = QGridLayout(ChecklistWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.list = QListWidget(ChecklistWidget)
        self.list.setObjectName(u"list")
        self.list.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)

        self.gridLayout.addWidget(self.list, 0, 0, 1, 1)


        self.retranslateUi(ChecklistWidget)

        QMetaObject.connectSlotsByName(ChecklistWidget)
    # setupUi

    def retranslateUi(self, ChecklistWidget):
        ChecklistWidget.setWindowTitle(QCoreApplication.translate("ChecklistWidget", u"Form", None))
    # retranslateUi

