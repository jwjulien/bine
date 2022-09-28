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
    QLineEdit, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(621, 58)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.check = QCheckBox(Form)
        self.check.setObjectName(u"check")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check.sizePolicy().hasHeightForWidth())
        self.check.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.check)

        self.stacker = QStackedWidget(Form)
        self.stacker.setObjectName(u"stacker")
        self.view = QWidget()
        self.view.setObjectName(u"view")
        self.verticalLayout_2 = QVBoxLayout(self.view)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text = QLabel(self.view)
        self.text.setObjectName(u"text")

        self.verticalLayout_2.addWidget(self.text)

        self.stacker.addWidget(self.view)
        self.editor = QWidget()
        self.editor.setObjectName(u"editor")
        self.verticalLayout = QVBoxLayout(self.editor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.edit = QLineEdit(self.editor)
        self.edit.setObjectName(u"edit")

        self.verticalLayout.addWidget(self.edit)

        self.stacker.addWidget(self.editor)

        self.horizontalLayout.addWidget(self.stacker)


        self.retranslateUi(Form)

        self.stacker.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

