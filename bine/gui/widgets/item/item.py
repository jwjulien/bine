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
from bine.libraries.undo.item import TextChange, CheckChange
from bine.libraries.block import Block
from bine.settings import settings




# ======================================================================================================================
# Checklist Item Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class ChecklistItemWidget(QtWidgets.QWidget):
    """A widget that represents a single checklist item."""

    contentChanged = QtCore.Signal(ItemModel)
    command = QtCore.Signal(QtGui.QUndoCommand)

    def __init__(self, parent: QtWidgets.QWidget, item: ItemModel):
        super().__init__(parent)
        self.ui = Ui_ChecklistItemWidget()
        self.ui.setupUi(self)

        self._item = item
        self._block = Block()
        self.update()

        self.ui.checkbox.stateChanged.connect(self._checked)
        self.ui.stack.setCurrentWidget(self.ui.view_mode)
        self.ui.viewer.doubleClicked.connect(self.edit)
        self.ui.editor.accept.connect(self.save)
        self.ui.editor.reject.connect(self.revert)


# ----------------------------------------------------------------------------------------------------------------------
    def item(self) -> ItemModel:
        return self._item


# ----------------------------------------------------------------------------------------------------------------------
    def _checked(self, state: QtCore.Qt.CheckState) -> None:
        if self._block.unlocked:
            checked = state == QtCore.Qt.Checked
            self.command.emit(CheckChange(self, checked))


# ----------------------------------------------------------------------------------------------------------------------
    def setChecked(self, checked: bool) -> None:
        with self._block:
            self._item.checked = checked
        self.update()
        self.contentChanged.emit(self._item)


# ----------------------------------------------------------------------------------------------------------------------
    def setText(self, text: str) -> None:
        with self._block:
            self._item.text = text
        self.update()
        self.contentChanged.emit(self._item)


# ----------------------------------------------------------------------------------------------------------------------
    def toggle(self) -> None:
        """Toggle the currently checked state for this item."""
        self.ui.checkbox.toggle()


# ----------------------------------------------------------------------------------------------------------------------
    def update(self) -> None:
        """Update the GUI from the associated item."""
        with self._block:
            self.ui.checkbox.setCheckState(QtCore.Qt.Checked if self._item.checked else QtCore.Qt.Unchecked)
            self.ui.viewer.setText(self._item.text)
            self.ui.children.setVisible(bool(self._item.children))
            self.ui.progress.setValue(self._item.progress)
            self.ui.count.setText(str(len(self._item.children)))

        style = 'QLabel { color: red; }' if settings.highlight_duplicates and self._item.duplicate else ''
        self.ui.viewer.setStyleSheet(style)

        self.ui.stack.setCurrentWidget(self.ui.view_mode)


# ----------------------------------------------------------------------------------------------------------------------
    def edit(self) -> None:
        """Switch to edit mode and show the editor with the current item text."""
        self.ui.editor.setText(self._item.text)
        self.ui.editor.setCursorPosition(len(self._item.text))
        self.ui.stack.setCurrentWidget(self.ui.edit_mode)
        self.ui.editor.setFocus()


# ----------------------------------------------------------------------------------------------------------------------
    def save(self) -> None:
        """Switch to view mode and store the state of the editor back to the item and the viewer."""
        text = self.ui.editor.text()
        if text != self._item.text:
            self.command.emit(TextChange(self, text))
        self.ui.stack.setCurrentWidget(self.ui.view_mode)


# ----------------------------------------------------------------------------------------------------------------------
    def revert(self) -> None:
        """Exit edit mode but revert the changes from the editor."""
        self.update()




# End of File
