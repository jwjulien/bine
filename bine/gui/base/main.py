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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QVBoxLayout,
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
        self.actionInsert = QAction(MainWindow)
        self.actionInsert.setObjectName(u"actionInsert")
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
        self.actionCheckAll = QAction(MainWindow)
        self.actionCheckAll.setObjectName(u"actionCheckAll")
        self.actionUncheckAll = QAction(MainWindow)
        self.actionUncheckAll.setObjectName(u"actionUncheckAll")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionToggleSelected = QAction(MainWindow)
        self.actionToggleSelected.setObjectName(u"actionToggleSelected")
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionEdit.setEnabled(False)
        self.actionHighlightDuplicates = QAction(MainWindow)
        self.actionHighlightDuplicates.setObjectName(u"actionHighlightDuplicates")
        self.actionHighlightDuplicates.setCheckable(True)
        self.actionAutoCheck = QAction(MainWindow)
        self.actionAutoCheck.setObjectName(u"actionAutoCheck")
        self.actionAutoCheck.setCheckable(True)
        self.actionAutoSort = QAction(MainWindow)
        self.actionAutoSort.setObjectName(u"actionAutoSort")
        self.actionAutoSort.setCheckable(True)
        self.actionCheckChildren = QAction(MainWindow)
        self.actionCheckChildren.setObjectName(u"actionCheckChildren")
        self.actionCheckChildren.setCheckable(True)
        self.actionHideChecked = QAction(MainWindow)
        self.actionHideChecked.setObjectName(u"actionHideChecked")
        self.actionHideChecked.setCheckable(True)
        self.main = QWidget(MainWindow)
        self.main.setObjectName(u"main")
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.stack = QStackedWidget(self.main)
        self.stack.setObjectName(u"stack")
        self.placeholder_page = QWidget()
        self.placeholder_page.setObjectName(u"placeholder_page")
        self.verticalLayout_3 = QVBoxLayout(self.placeholder_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 236, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.placeholder = QLabel(self.placeholder_page)
        self.placeholder.setObjectName(u"placeholder")

        self.horizontalLayout.addWidget(self.placeholder)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 236, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.stack.addWidget(self.placeholder_page)
        self.tabs_page = QWidget()
        self.tabs_page.setObjectName(u"tabs_page")
        self.verticalLayout = QVBoxLayout(self.tabs_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabs = QTabWidget(self.tabs_page)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)

        self.verticalLayout.addWidget(self.tabs)

        self.stack.addWidget(self.tabs_page)

        self.verticalLayout_2.addWidget(self.stack)

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
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionInsert)
        self.menuEdit.addAction(self.actionEdit)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionMoveUp)
        self.menuEdit.addAction(self.actionMoveDown)
        self.menuEdit.addAction(self.actionIndent)
        self.menuEdit.addAction(self.actionDedent)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCheckAll)
        self.menuEdit.addAction(self.actionUncheckAll)
        self.menuEdit.addAction(self.actionToggleSelected)
        self.menuExport.addAction(self.menuHTML.menuAction())
        self.menuHTML.addAction(self.actionExportHtmlWhite)
        self.menuHTML.addAction(self.actionExportHtmlSlate)
        self.menuSettings.addAction(self.actionHighlightDuplicates)
        self.menuSettings.addAction(self.actionAutoSort)
        self.menuSettings.addAction(self.actionAutoCheck)
        self.menuSettings.addAction(self.actionHideChecked)

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
        self.actionInsert.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
#if QT_CONFIG(shortcut)
        self.actionInsert.setShortcut(QCoreApplication.translate("MainWindow", u"Ins", None))
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
        self.actionCheckAll.setText(QCoreApplication.translate("MainWindow", u"Check All", None))
        self.actionUncheckAll.setText(QCoreApplication.translate("MainWindow", u"Uncheck All", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actionToggleSelected.setText(QCoreApplication.translate("MainWindow", u"Toggle Selected", None))
#if QT_CONFIG(shortcut)
        self.actionToggleSelected.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.actionEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
#if QT_CONFIG(shortcut)
        self.actionEdit.setShortcut(QCoreApplication.translate("MainWindow", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.actionHighlightDuplicates.setText(QCoreApplication.translate("MainWindow", u"Highlight Duplicates", None))
#if QT_CONFIG(statustip)
        self.actionHighlightDuplicates.setStatusTip(QCoreApplication.translate("MainWindow", u"Highlight items when items with the same text appear elsewhere in the document.", None))
#endif // QT_CONFIG(statustip)
        self.actionAutoCheck.setText(QCoreApplication.translate("MainWindow", u"Auto-check", None))
#if QT_CONFIG(statustip)
        self.actionAutoCheck.setStatusTip(QCoreApplication.translate("MainWindow", u"Tie children check state to parent.", None))
#endif // QT_CONFIG(statustip)
        self.actionAutoSort.setText(QCoreApplication.translate("MainWindow", u"Auto-sort", None))
#if QT_CONFIG(statustip)
        self.actionAutoSort.setStatusTip(QCoreApplication.translate("MainWindow", u"Keep lists sorted in alphabetical order as items are added and changed.", None))
#endif // QT_CONFIG(statustip)
        self.actionCheckChildren.setText(QCoreApplication.translate("MainWindow", u"Mark children checked", None))
#if QT_CONFIG(statustip)
        self.actionCheckChildren.setStatusTip(QCoreApplication.translate("MainWindow", u"Cascade checks on parents to all children.", None))
#endif // QT_CONFIG(statustip)
        self.actionHideChecked.setText(QCoreApplication.translate("MainWindow", u"Hide Checked", None))
        self.placeholder.setText(QCoreApplication.translate("MainWindow", u"To get started, create a new tab or open a document.", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
        self.menuHTML.setTitle(QCoreApplication.translate("MainWindow", u"HTML", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

