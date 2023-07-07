# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_ChecklistItemWidget(object):
    def setupUi(self, ChecklistItemWidget):
        if not ChecklistItemWidget.objectName():
            ChecklistItemWidget.setObjectName(u"ChecklistItemWidget")
        ChecklistItemWidget.resize(400, 42)
        self.horizontalLayout = QHBoxLayout(ChecklistItemWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkbox = QCheckBox(ChecklistItemWidget)
        self.checkbox.setObjectName(u"checkbox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox.sizePolicy().hasHeightForWidth())
        self.checkbox.setSizePolicy(sizePolicy)
        self.checkbox.setTristate(True)

        self.horizontalLayout.addWidget(self.checkbox)

        self.chevron = QLabel(ChecklistItemWidget)
        self.chevron.setObjectName(u"chevron")
        self.chevron.setMaximumSize(QSize(18, 18))
        self.chevron.setPixmap(QPixmap(u"../bine/assets/icons/chevron-right-24.png"))
        self.chevron.setScaledContents(True)

        self.horizontalLayout.addWidget(self.chevron)


        self.retranslateUi(ChecklistItemWidget)

        QMetaObject.connectSlotsByName(ChecklistItemWidget)
    # setupUi

    def retranslateUi(self, ChecklistItemWidget):
        ChecklistItemWidget.setWindowTitle(QCoreApplication.translate("ChecklistItemWidget", u"Form", None))
        self.checkbox.setText(QCoreApplication.translate("ChecklistItemWidget", u"Checklist item", None))
        self.chevron.setText("")
    # retranslateUi

