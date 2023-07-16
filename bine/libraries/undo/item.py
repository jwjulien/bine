# ======================================================================================================================
#      File:  /bine/libraries/undo/item.py
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
"""Undo support for tree options."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtGui, QtWidgets

from bine.model.item import ItemModel




# ======================================================================================================================
# Item Text Command
# ----------------------------------------------------------------------------------------------------------------------
class TextChange(QtGui.QUndoCommand):
    """Supports undo/redo for a single item text."""
    def __init__(self, widget: QtWidgets.QWidget, text: str):
        super().__init__(f'change "{widget.item().text}" to "{text}"')
        self._widget = widget
        self._before = widget.item().text
        self._after = text


# ----------------------------------------------------------------------------------------------------------------------
    def redo(self):
        self._widget.setText(self._after)


# ----------------------------------------------------------------------------------------------------------------------
    def undo(self):
        self._widget.setText(self._before)




# ======================================================================================================================
# Item Check State Command
# ----------------------------------------------------------------------------------------------------------------------
class CheckChange(QtGui.QUndoCommand):
    """Supports undo/redo for a single item checkbox state."""
    def __init__(self, widget: QtWidgets.QWidget, checked: bool):
        super().__init__(f"{'' if checked else 'un'}check \"{widget.item().text}\"")
        self._widget = widget
        self._before = widget.item().checked
        self._after = checked


# ----------------------------------------------------------------------------------------------------------------------
    def redo(self):
        self._widget.setChecked(self._after)


# ----------------------------------------------------------------------------------------------------------------------
    def undo(self):
        self._widget.setChecked(self._before)




# ======================================================================================================================
# Delete Item Undo Class
# ----------------------------------------------------------------------------------------------------------------------
class Delete(QtGui.QUndoCommand):
    """Supports deleting an item from a list."""
    def __init__(self,
                 widget: QtWidgets.QTreeWidget,
                 node: QtWidgets.QTreeWidgetItem):
        item = node.data(0, QtCore.Qt.UserRole)
        super().__init__(f'delete "{item.text}"')
        self._widget: QtWidgets.QTreeWidget = widget
        self._node: QtWidgets.QTreeWidgetItem = node
        self._parent: QtWidgets.QTreeWidgetItem = node.parent()
        self._item: ItemModel = item
        self._index: int = item.row()


# ----------------------------------------------------------------------------------------------------------------------
    def redo(self):
        self._widget.blockSignals(True)
        if self._parent:
            self._parent.removeChild(self._node)
        else:
            self._widget.takeTopLevelItem(self._index)
        self._widget.blockSignals(False)
        self._item.parent.children.pop(self._index)


# ----------------------------------------------------------------------------------------------------------------------
    def undo(self):
        self._widget.blockSignals(True)
        if self._parent:
            self._parent.insertChild(self._index, self._node)
        else:
            self._widget.insertTopLevelItem(self._index, self._node)
        self._widget.blockSignals(False)
        self._item.parent.children.insert(self._index, self._item)




# ======================================================================================================================
# Insert Item Undo Class
# ----------------------------------------------------------------------------------------------------------------------
class CommandItemInsert(QtGui.QUndoCommand):
    """Supports undoing the insertion of an item into the tree."""
    def __init__(self,
                 widget: QtWidgets.QTreeWidget,
                 node: QtWidgets.QTreeWidgetItem,
                 selected: QtWidgets.QTreeWidgetItem,
                 root: ItemModel,
                 sibling: bool):
        item = node.data(0, QtCore.Qt.UserRole)
        description = f'insert "{item.text}"'
        super().__init__(description)
        self._widget: QtWidgets.QTreeWidget = widget
        self._node: QtWidgets.QTreeWidgetItem = node
        self._selected: QtWidgets.QTreeWidgetItem = selected
        self._root: ItemModel = root
        self._sibling: bool = sibling
        self._item: ItemModel = item


# ----------------------------------------------------------------------------------------------------------------------
    def redo(self):
        self._widget.blockSignals(True)
        if not self._selected:
            self._item.parent = self._root
            self._root.children.append(self._item)
            self._widget.addTopLevelItem(self._node)
        else:
            selected_node = self._selected
            selected_item: ItemModel = selected_node.data(0, QtCore.Qt.UserRole)
            self._item.parent = selected_item
            if self._sibling:
                selected_item.parent.children.append(self._item)
                selected_node.parent().addChild(self._node)
            else:
                selected_item.children.append(self._item)
                selected_node.addChild(self._node)
                selected_node.setExpanded(True)
        self._widget.blockSignals(False)


# ----------------------------------------------------------------------------------------------------------------------
    def undo(self):
        self._widget.blockSignals(True)
        if not self._selected:
            self._widget.takeTopLevelItem(self._widget.indexOfTopLevelItem(self._node))
        else:
            self._node.parent().removeChild(self._node)
        self._item.parent.children.pop(self._item.row())
        self._widget.blockSignals(False)





# ======================================================================================================================
# Move Item Undo Class
# ----------------------------------------------------------------------------------------------------------------------
class CommandItemMove(QtGui.QUndoCommand):
    """Undo command for moving items around the tree."""
    def __init__(self,
                 widget: QtWidgets.QTreeWidget,
                 node: QtWidgets.QTreeWidgetItem):
        item = node.data(0, QtCore.Qt.UserRole)
        description = f'delete "{item.text}"'
        super().__init__(description)
        self._widget: QtWidgets.QTreeWidget = widget
        self._node: QtWidgets.QTreeWidgetItem = node
        self._parent: QtWidgets.QTreeWidgetItem = node.parent()
        self._item: ItemModel = item
        self._index: int = item.row()


# ----------------------------------------------------------------------------------------------------------------------
    def redo(self):
        self._widget.blockSignals(True)
        if self._parent:
            self._parent.removeChild(self._node)
        else:
            self._widget.takeTopLevelItem(self._index)
        self._widget.blockSignals(False)
        self._item.parent.children.pop(self._index)


# ----------------------------------------------------------------------------------------------------------------------
    def undo(self):
        self._widget.blockSignals(True)
        if self._parent:
            self._parent.insertChild(self._index, self._node)
        else:
            self._widget.insertTopLevelItem(self._index, self._node)
        self._widget.blockSignals(False)
        self._item.parent.children.insert(self._index, self._item)







# End of File
