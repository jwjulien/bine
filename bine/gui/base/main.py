# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 579)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionSave_a_Copy = QAction(MainWindow)
        self.actionSave_a_Copy.setObjectName(u"actionSave_a_Copy")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionContents = QAction(MainWindow)
        self.actionContents.setObjectName(u"actionContents")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        self.actionPreview = QAction(MainWindow)
        self.actionPreview.setObjectName(u"actionPreview")
        self.actionInsertSibling = QAction(MainWindow)
        self.actionInsertSibling.setObjectName(u"actionInsertSibling")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionDelete.setEnabled(False)
        self.actionExportHtmlSlate = QAction(MainWindow)
        self.actionExportHtmlSlate.setObjectName(u"actionExportHtmlSlate")
        self.actionExportHtmlWhite = QAction(MainWindow)
        self.actionExportHtmlWhite.setObjectName(u"actionExportHtmlWhite")
        self.actionHeadingsHashes = QAction(MainWindow)
        self.actionHeadingsHashes.setObjectName(u"actionHeadingsHashes")
        self.actionHeadingsHashes.setCheckable(True)
        self.actionHeadingsBars = QAction(MainWindow)
        self.actionHeadingsBars.setObjectName(u"actionHeadingsBars")
        self.actionHeadingsBars.setCheckable(True)
        self.actionTristate = QAction(MainWindow)
        self.actionTristate.setObjectName(u"actionTristate")
        self.actionTristate.setCheckable(True)
        self.actionCloseTab = QAction(MainWindow)
        self.actionCloseTab.setObjectName(u"actionCloseTab")
        self.actionInsertChild = QAction(MainWindow)
        self.actionInsertChild.setObjectName(u"actionInsertChild")
        self.actionDedent = QAction(MainWindow)
        self.actionDedent.setObjectName(u"actionDedent")
        self.actionDedent.setEnabled(False)
        self.actionIndent = QAction(MainWindow)
        self.actionIndent.setObjectName(u"actionIndent")
        self.actionIndent.setEnabled(False)
        self.actionMoveUp = QAction(MainWindow)
        self.actionMoveUp.setObjectName(u"actionMoveUp")
        self.actionMoveUp.setEnabled(False)
        self.actionMoveDown = QAction(MainWindow)
        self.actionMoveDown.setObjectName(u"actionMoveDown")
        self.actionMoveDown.setEnabled(False)
        self.actionExpandAll = QAction(MainWindow)
        self.actionExpandAll.setObjectName(u"actionExpandAll")
        self.actionCollapseAll = QAction(MainWindow)
        self.actionCollapseAll.setObjectName(u"actionCollapseAll")
        self.main = QWidget(MainWindow)
        self.main.setObjectName(u"main")
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabs = QTabWidget(self.main)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)

        self.verticalLayout.addWidget(self.tabs)

        MainWindow.setCentralWidget(self.main)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 819, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuExport = QMenu(self.menubar)
        self.menuExport.setObjectName(u"menuExport")
        self.menuHTML = QMenu(self.menuExport)
        self.menuHTML.setObjectName(u"menuHTML")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSave_a_Copy)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionPreview)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCloseTab)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionInsertSibling)
        self.menuEdit.addAction(self.actionInsertChild)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionMoveUp)
        self.menuEdit.addAction(self.actionMoveDown)
        self.menuEdit.addAction(self.actionIndent)
        self.menuEdit.addAction(self.actionDedent)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionExpandAll)
        self.menuEdit.addAction(self.actionCollapseAll)
        self.menuExport.addAction(self.menuHTML.menuAction())
        self.menuHTML.addAction(self.actionExportHtmlWhite)
        self.menuHTML.addAction(self.actionExportHtmlSlate)
        self.menuSettings.addAction(self.actionTristate)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_a_Copy.setText(QCoreApplication.translate("MainWindow", u"Save a Copy...", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionContents.setText(QCoreApplication.translate("MainWindow", u"Contents", None))
#if QT_CONFIG(shortcut)
        self.actionContents.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
#if QT_CONFIG(shortcut)
        self.actionCut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print...", None))
        self.actionPreview.setText(QCoreApplication.translate("MainWindow", u"Print Preview...", None))
        self.actionInsertSibling.setText(QCoreApplication.translate("MainWindow", u"Insert Sibling", None))
#if QT_CONFIG(shortcut)
        self.actionInsertSibling.setShortcut(QCoreApplication.translate("MainWindow", u"Ins", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionExportHtmlSlate.setText(QCoreApplication.translate("MainWindow", u"Slate", None))
        self.actionExportHtmlWhite.setText(QCoreApplication.translate("MainWindow", u"White", None))
        self.actionHeadingsHashes.setText(QCoreApplication.translate("MainWindow", u"Hashes", None))
        self.actionHeadingsBars.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.actionTristate.setText(QCoreApplication.translate("MainWindow", u"Tristate Checkboxes", None))
        self.actionCloseTab.setText(QCoreApplication.translate("MainWindow", u"Close Tab", None))
#if QT_CONFIG(shortcut)
        self.actionCloseTab.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionInsertChild.setText(QCoreApplication.translate("MainWindow", u"Insert Child", None))
#if QT_CONFIG(shortcut)
        self.actionInsertChild.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Ins", None))
#endif // QT_CONFIG(shortcut)
        self.actionDedent.setText(QCoreApplication.translate("MainWindow", u"Dedent", None))
#if QT_CONFIG(shortcut)
        self.actionDedent.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Left", None))
#endif // QT_CONFIG(shortcut)
        self.actionIndent.setText(QCoreApplication.translate("MainWindow", u"Indent", None))
#if QT_CONFIG(shortcut)
        self.actionIndent.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Right", None))
#endif // QT_CONFIG(shortcut)
        self.actionMoveUp.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
#if QT_CONFIG(shortcut)
        self.actionMoveUp.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionMoveDown.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
#if QT_CONFIG(shortcut)
        self.actionMoveDown.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionExpandAll.setText(QCoreApplication.translate("MainWindow", u"Expand All", None))
#if QT_CONFIG(shortcut)
        self.actionExpandAll.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+.", None))
#endif // QT_CONFIG(shortcut)
        self.actionCollapseAll.setText(QCoreApplication.translate("MainWindow", u"Collapse All", None))
#if QT_CONFIG(shortcut)
        self.actionCollapseAll.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+,", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
        self.menuHTML.setTitle(QCoreApplication.translate("MainWindow", u"HTML", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

