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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLineEdit,
    QSizePolicy, QSplitter, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

from bine.gui.widgets.editor import MarkdownSpellTextEdit

class Ui_Tab(object):
    def setupUi(self, Tab):
        if not Tab.objectName():
            Tab.setObjectName(u"Tab")
        Tab.resize(813, 531)
        self.verticalLayout = QVBoxLayout(Tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLineEdit(Tab)
        self.title.setObjectName(u"title")

        self.verticalLayout.addWidget(self.title)

        self.splitter = QSplitter(Tab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.description = MarkdownSpellTextEdit(self.splitter)
        self.description.setObjectName(u"description")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(10)
        self.description.setFont(font)
        self.splitter.addWidget(self.description)
        self.tree = QTreeWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree.setHeaderItem(__qtreewidgetitem)
        self.tree.setObjectName(u"tree")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tree.sizePolicy().hasHeightForWidth())
        self.tree.setSizePolicy(sizePolicy1)
        self.tree.setDragEnabled(True)
        self.tree.setDragDropMode(QAbstractItemView.InternalMove)
        self.tree.setDefaultDropAction(Qt.MoveAction)
        self.tree.setAlternatingRowColors(True)
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree.setIndentation(15)
        self.tree.setHeaderHidden(True)
        self.splitter.addWidget(self.tree)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(Tab)

        QMetaObject.connectSlotsByName(Tab)
    # setupUi

    def retranslateUi(self, Tab):
        Tab.setWindowTitle(QCoreApplication.translate("Tab", u"Form", None))
    # retranslateUi

