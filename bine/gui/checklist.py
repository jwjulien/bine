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
import os
from typing import List

from PySide6 import QtCore, QtGui, QtWidgets

from bine.gui.base.checklist import Ui_ChecklistWidget
from bine.gui.widgets.item import ChecklistItemWidget
from bine.model.item import ChecklistItem





# ======================================================================================================================
# Checklist Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class ChecklistWidget(QtWidgets.QWidget):
    """A tree and editor for a single document within a single tab of the GUI window."""

    contentChanged = QtCore.Signal()
    itemSelected = QtCore.Signal(ChecklistItem)

    def __init__(self, parent: QtWidgets.QWidget, list: ChecklistItem, selected: ChecklistItem = None):
        super().__init__(parent)
        self.ui = Ui_ChecklistWidget()
        self.ui.setupUi(self)

        self._mouse_position: QtCore.QPoint = None

        self._list: ChecklistItem = list
        for child in self._list.children:
            widget = self._make_widget(child)
            self.ui.list.addItem(widget)
            if child == selected:
                self.ui.list.setCurrentItem(widget)

        self.popmenu = QtWidgets.QMenu(self)
        self.popmenu_insert = QtGui.QAction('Insert', self)
        self.popmenu.addAction(self.popmenu_insert)
        self.popmenu_delete = QtGui.QAction('Delete', self)
        self.popmenu_delete.setEnabled(bool(selected))
        self.popmenu.addAction(self.popmenu_delete)
        self.popmenu_insert.triggered.connect(self.insert)
        self.popmenu_delete.triggered.connect(self.delete)
        self.ui.list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.list.customContextMenuRequested.connect(lambda p: self.popmenu.exec(self.ui.list.mapToGlobal(p)))
        self.ui.list.currentItemChanged.connect(self._item_selected)
        self.ui.list.itemChanged.connect(self._item_changed)
        self.ui.list.itemSelectionChanged.connect(self._selection_changed)

        # Connect every event and print info for testing.
        # self.ui.list.currentItemChanged.connect(lambda current, previous: print('Current item changed:', current, previous))
        # self.ui.list.currentRowChanged.connect(lambda row: print('Current row changed:', row))
        # self.ui.list.currentTextChanged.connect(lambda text: print('Current text changed:', text))
        # self.ui.list.itemActivated.connect(lambda item: print('Activated:', item.data(QtCore.Qt.UserRole)))
        # self.ui.list.itemChanged.connect(lambda item: print('Changed:', item.data(QtCore.Qt.UserRole)))
        # self.ui.list.itemClicked.connect(lambda item: print('Clicked:', item.data(QtCore.Qt.UserRole)))
        # self.ui.list.itemDoubleClicked.connect(lambda item: print('Double Clicked:', item.data(QtCore.Qt.UserRole)))
        # self.ui.list.itemEntered.connect(lambda item: print('Entered:', item.data(QtCore.Qt.UserRole)))
        # self.ui.list.itemPressed.connect(lambda item: print('Pressed:', item.data(QtCore.Qt.UserRole)))
        # self.ui.list.itemSelectionChanged.connect(lambda: print('Selection Changed'))


# ----------------------------------------------------------------------------------------------------------------------
    def _make_widget(self, item: ChecklistItem) -> QtWidgets.QListWidgetItem:
        widget: QtWidgets.QListWidgetItem = QtWidgets.QListWidgetItem(item.text)
        widget.setFlags(widget.flags() | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsUserCheckable)
        widget.setCheckState(QtCore.Qt.Checked if item.checked else QtCore.Qt.Unchecked)
        widget.setData(QtCore.Qt.UserRole, item)

        icon = QtGui.QPixmap(os.path.join('bine', 'assets', 'icons', 'chevron-right-50.png'))

        self.ui.list.setItemWidget(widget, ChecklistItemWidget(None, item))
        return widget


# ----------------------------------------------------------------------------------------------------------------------
    def _item_selected(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem) -> None:
        item = current.data(QtCore.Qt.UserRole)
        print('Selected:', item)
        self.itemSelected.emit(item)


# ----------------------------------------------------------------------------------------------------------------------
    def _item_changed(self, widget: QtWidgets.QListWidgetItem) -> None:
        item = widget.data(QtCore.Qt.UserRole)
        print('Changed:', item)
        if item is None:
            return
        item.text = widget.text()
        item.checked = widget.checkState() == QtCore.Qt.Checked
        self.contentChanged.emit()
        # TODO: Remove empty items from the list.


# ----------------------------------------------------------------------------------------------------------------------
    def _selection_changed(self):
        selected = self.ui.list.selectedIndexes()
        self.popmenu_delete.setEnabled(len(selected) == 1)
        print('Selection changed:', selected)


# ----------------------------------------------------------------------------------------------------------------------
    def insert(self):
        """Called to insert a new item into the list at the current selected location.

        If no item in the list is currently selected then insert a new item at the end of the list.
        """
        indexes = self.ui.list.selectedIndexes()
        row = indexes[-1].row() if len(indexes) > 0 else self._list.childCount()

        item = ChecklistItem(self._list)
        self._list.children.insert(row, item)

        widget = self._make_widget(item)
        self.ui.list.insertItem(row, widget)
        self.ui.list.editItem(widget)


# ----------------------------------------------------------------------------------------------------------------------
    def delete(self):
        """Fires to delete the currently selected item from the list."""
        indexes = self.ui.list.selectedIndexes()
        row = indexes[-1].row() if len(indexes) > 0 else self._list.childCount()
        print('Delete row', row)
        self.ui.list.takeItem(row)
        self._list.children.pop(row)
        self.contentChanged.emit()
        self.itemSelected.emit(self._list)


# # ----------------------------------------------------------------------------------------------------------------------
#     def move_up(self):
#         """Fires when the user selects the move up menu option.  Moves the item up one position."""
#         selection = self._selected_indexes()
#         if not selection:
#             return
#         for node in selection:
#             item: ChecklistItem = node.data(0, QtCore.Qt.UserRole)
#             index = item.row()
#             if index > 0:
#                 item.parent.children.pop(index)
#                 item.parent.children.insert(index - 1, item)

#                 parent = node.parent()
#                 if parent:
#                     parent.removeChild(node)
#                     parent.insertChild(index - 1, node)
#                 else:
#                     self.ui.columns.takeTopLevelItem(index)
#                     self.ui.columns.insertTopLevelItem(index - 1, node)

#                 self.ui.columns.setCurrentItem(node, 0)

#         self.contentChanged.emit()


# # ----------------------------------------------------------------------------------------------------------------------
#     def move_down(self):
#         """Fires when the user selects the move down menu option.  Moves the item down one position."""
#         selection = self._selected_indexes(True)
#         if not selection:
#             return
#         for node in selection:
#             item: ChecklistItem = node.data(0, QtCore.Qt.UserRole)
#             index = item.row()
#             if index < (len(item.parent.children) - 1):
#                 item.parent.children.pop(index)
#                 item.parent.children.insert(index + 1, item)

#                 parent = node.parent()
#                 if parent:
#                     parent.removeChild(node)
#                     parent.insertChild(index + 1, node)
#                 else:
#                     self.ui.columns.takeTopLevelItem(index)
#                     self.ui.columns.insertTopLevelItem(index + 1, node)

#                 self.ui.columns.setCurrentItem(node, 0)

#         self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
#     def indent(self):
#         """Fires when the user selects the indent menu option.  Moves the item to be a sibling of the item above."""
#         selection = self._selected_indexes()
#         if not selection:
#             return
#         top = selection[0]
#         parent = top.parent()
#         if parent:
#             parent_item: ChecklistItem = parent.data(0, QtCore.Qt.UserRole)
#             above = parent.child(parent.indexOfChild(top) - 1)
#         else:
#             parent_item: ChecklistItem = self.model.root
#             above = self.ui.columns.topLevelItem(self.ui.columns.indexOfTopLevelItem(top) - 1)
#         above_item: ChecklistItem = above.data(0, QtCore.Qt.UserRole)

#         for node in selection:
#             # Move the item in the model.
#             item: ChecklistItem = node.data(0, QtCore.Qt.UserRole)
#             parent_item.children.pop(item.row())
#             above_item.children.append(item)
#             item.parent = above_item

#             # Move the item in the tree.
#             if parent:
#                 parent.removeChild(node)
#             else:
#                 self.ui.columns.takeTopLevelItem(item.row())
#             above.addChild(node)

#             self.ui.columns.setCurrentItem(node, 0)

#         self.contentChanged.emit()


# # ----------------------------------------------------------------------------------------------------------------------
#     def dedent(self):
#         """Fires when the user selects the dedent menu option.  Moves the selected item up to the parent level."""
#         selection = self._selected_indexes(True)
#         if not selection:
#             return
#         for node in selection:
#             item: ChecklistItem = node.data(0, QtCore.Qt.UserRole)
#             if item.parent.parent:
#                 # Move the node in the model.
#                 item.parent.children.pop(item.row())
#                 index = item.parent.row() + 1
#                 item.parent.parent.children.insert(index, item)
#                 item.parent = item.parent.parent

#                 # Move the node within the tree.
#                 parent = node.parent()
#                 parent.removeChild(node)

#                 if parent.childCount() == 0:
#                     parent_item = parent.data(0, QtCore.Qt.UserRole)
#                     parent.setCheckState(0, QtCore.Qt.Checked if parent_item.checked else QtCore.Qt.Unchecked)

#                 grandparent = parent.parent()
#                 if grandparent:
#                     grandparent.insertChild(index, node)
#                 else:
#                     self.ui.columns.insertTopLevelItem(index, node)

#                 self.ui.columns.setCurrentItem(node, 0)

#         self.contentChanged.emit()




# End of File
