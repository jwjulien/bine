# ======================================================================================================================
#      File:  /bine/gui/widgets/item.py
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
"""A custom widget to represent an "item" in a list."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtGui, QtWidgets

from bine.gui.base.item import Ui_ChecklistItemWidget
from bine.model.item import ItemModel




# ======================================================================================================================
# Checklist Item Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class ChecklistItemWidget(QtWidgets.QWidget):
    """A widget that represents a single checklist item."""

    contentChanged = QtCore.Signal(ItemModel)

    def __init__(self, parent: QtWidgets.QWidget, item: ItemModel):
        super().__init__(parent)
        self.ui = Ui_ChecklistItemWidget()
        self.ui.setupUi(self)

        self._item = item
        self._updating = False
        self.update()

        self.ui.checkbox.stateChanged.connect(self._checked)
        self.ui.stack.setCurrentWidget(self.ui.view_mode)
        self.ui.viewer.doubleClicked.connect(self.edit)
        self.ui.editor.doneEditing.connect(self.view)


# ----------------------------------------------------------------------------------------------------------------------
    def _checked(self, state: QtCore.Qt.CheckState) -> None:
        if not self._updating:
            self._item.checked = state == QtCore.Qt.Checked
            self.contentChanged.emit(self._item)


# ----------------------------------------------------------------------------------------------------------------------
    def update(self) -> None:
        """Update the GUI from the associated item."""
        self._updating = True
        self.ui.checkbox.setCheckState(QtCore.Qt.Checked if self._item.checked else QtCore.Qt.Unchecked)
        self.ui.viewer.setText(self._item.text)
        self.ui.children.setVisible(bool(self._item.children))
        self.ui.progress.setValue(self._item.progress)
        self.ui.count.setText(str(len(self._item.children)))
        self._updating = False

        self.ui.stack.setCurrentWidget(self.ui.view_mode)


# ----------------------------------------------------------------------------------------------------------------------
    def edit(self) -> None:
        """Switch to edit mode and show the editor with the current item text."""
        self.ui.editor.setText(self._item.text)
        self.ui.editor.setCursorPosition(len(self._item.text))
        self.ui.stack.setCurrentWidget(self.ui.edit_mode)
        self.ui.editor.setFocus()


# ----------------------------------------------------------------------------------------------------------------------
    def view(self) -> None:
        """Switch to view mode and store the state of the editor back to the item and the viewer."""
        self._item.text = self.ui.editor.text()
        self.contentChanged.emit(self._item)
        self.update()




# End of File
