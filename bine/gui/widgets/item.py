# ======================================================================================================================
#      File:  /bine/gui/checklist.py
#   Project:  Bine
#    Author:  Jared Julien <jaredjulien@exsystems.net>
# Copyright:  (c) 2022 Jared Julien, eX Systems
# ---------------------------------------------------------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ----------------------------------------------------------------------------------------------------------------------
"""Glorified extension of a QListWidget to represent a single Checklist node from a document."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtGui, QtWidgets, QtPrintSupport

from bine.gui.base.item import Ui_ChecklistItemWidget
from bine.model.item import ChecklistItem





# ======================================================================================================================
# Checklist Item Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class ChecklistItemWidget(QtWidgets.QWidget):
    """A tree and editor for a single document within a single tab of the GUI window."""

    contentChanged = QtCore.Signal()
    itemSelected = QtCore.Signal(ChecklistItem)

    def __init__(self, parent: QtWidgets.QWidget, item: ChecklistItem):
        super().__init__(parent)
        self.ui = Ui_ChecklistItemWidget()
        self.ui.setupUi(self)

        self.ui.checkbox.setText(item.text)
        self.ui.checkbox.setCheckState(QtCore.Qt.Checked if item.checked else QtCore.Qt.Unchecked)
        self.ui.chevron.setVisible(bool(item.children))






# End of File
