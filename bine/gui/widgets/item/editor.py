# ======================================================================================================================
#      File:  /bine/gui/widgets/item_editor.py
#   Project:  Bine
#    Author:  Jared Julien <jaredjulien@exsystems.net>
# Copyright:  (c) 2023 Jared Julien, eX Systems
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
"""Extension of the QLineEdit widget fto gain event support."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtGui, QtWidgets




# ======================================================================================================================
# Item Editor Class
# ----------------------------------------------------------------------------------------------------------------------
class ItemEditor(QtWidgets.QLineEdit):
    focusLost = QtCore.Signal()
    escapePressed = QtCore.Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.installEventFilter(self)


# ----------------------------------------------------------------------------------------------------------------------
    def focusOutEvent(self, event: QtGui.QFocusEvent) -> None:
        if event.reason() == QtCore.Qt.MouseFocusReason:
            self.focusLost.emit()
        return super().focusOutEvent(event)


# ----------------------------------------------------------------------------------------------------------------------
    def eventFilter(self, widget: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if widget is self and event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Escape:
                self.escapePressed.emit()
                return True
        return False




# End of File
