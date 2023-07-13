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
    QProgressBar, QSizePolicy, QStackedWidget, QWidget)

from bine.gui.widgets.item.editor import ItemEditor
from bine.gui.widgets.item.viewer import ViewerLabel

class Ui_ChecklistItemWidget(object):
    def setupUi(self, ChecklistItemWidget):
        if not ChecklistItemWidget.objectName():
            ChecklistItemWidget.setObjectName(u"ChecklistItemWidget")
        ChecklistItemWidget.resize(473, 24)
        self.horizontalLayout_2 = QHBoxLayout(ChecklistItemWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkbox = QCheckBox(ChecklistItemWidget)
        self.checkbox.setObjectName(u"checkbox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox.sizePolicy().hasHeightForWidth())
        self.checkbox.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.checkbox)

        self.stack = QStackedWidget(ChecklistItemWidget)
        self.stack.setObjectName(u"stack")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy1)
        self.view_mode = QWidget()
        self.view_mode.setObjectName(u"view_mode")
        self.horizontalLayout_4 = QHBoxLayout(self.view_mode)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.viewer = ViewerLabel(self.view_mode)
        self.viewer.setObjectName(u"viewer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.viewer.sizePolicy().hasHeightForWidth())
        self.viewer.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.viewer)

        self.stack.addWidget(self.view_mode)
        self.edit_mode = QWidget()
        self.edit_mode.setObjectName(u"edit_mode")
        self.horizontalLayout_3 = QHBoxLayout(self.edit_mode)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.editor = ItemEditor(self.edit_mode)
        self.editor.setObjectName(u"editor")

        self.horizontalLayout_3.addWidget(self.editor)

        self.stack.addWidget(self.edit_mode)

        self.horizontalLayout_2.addWidget(self.stack)

        self.children = QWidget(ChecklistItemWidget)
        self.children.setObjectName(u"children")
        self.horizontalLayout = QHBoxLayout(self.children)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.progress = QProgressBar(self.children)
        self.progress.setObjectName(u"progress")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy3)
        self.progress.setValue(24)
        self.progress.setTextVisible(False)

        self.horizontalLayout.addWidget(self.progress)

        self.count = QLabel(self.children)
        self.count.setObjectName(u"count")

        self.horizontalLayout.addWidget(self.count)

        self.chevron = QLabel(self.children)
        self.chevron.setObjectName(u"chevron")
        self.chevron.setMaximumSize(QSize(18, 18))
        self.chevron.setPixmap(QPixmap(u"bine/assets/icons/chevron-right-24.png"))
        self.chevron.setScaledContents(True)

        self.horizontalLayout.addWidget(self.chevron)


        self.horizontalLayout_2.addWidget(self.children)


        self.retranslateUi(ChecklistItemWidget)

        self.stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ChecklistItemWidget)
    # setupUi

    def retranslateUi(self, ChecklistItemWidget):
        ChecklistItemWidget.setWindowTitle(QCoreApplication.translate("ChecklistItemWidget", u"Form", None))
        self.checkbox.setText("")
        self.viewer.setText(QCoreApplication.translate("ChecklistItemWidget", u"Item Text", None))
        self.count.setText(QCoreApplication.translate("ChecklistItemWidget", u"0", None))
        self.chevron.setText("")
    # retranslateUi

