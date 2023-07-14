# ======================================================================================================================
#      File:  /bine/gui/widgets/checklist.py
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
from PySide6 import QtCore, QtGui, QtWidgets

from bine.gui.base.checklist import Ui_ChecklistWidget
from bine.gui.widgets.item.item import ChecklistItemWidget
from bine.model.item import ItemModel




# ======================================================================================================================
# Checklist Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class ChecklistWidget(QtWidgets.QWidget):
    """A widget that contains a QListWidget of ItemModel objects to be used in a column view."""

    contentChanged = QtCore.Signal()
    itemSelected = QtCore.Signal(ItemModel)

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.ui = Ui_ChecklistWidget()
        self.ui.setupUi(self)

        self._mouse_position: QtCore.QPoint = None
        self._list: ItemModel = None

        self.ui.children.setVisible(False)

        self.popmenu = QtWidgets.QMenu(self)
        self.popmenu_insert = QtGui.QAction('Insert', self)
        self.popmenu.addAction(self.popmenu_insert)
        self.popmenu_delete = QtGui.QAction('Delete', self)
        # self.popmenu_delete.setEnabled(bool(selected))
        self.popmenu.addAction(self.popmenu_delete)
        self.popmenu_insert.triggered.connect(self.add)
        self.popmenu_delete.triggered.connect(self.delete)

        self.ui.items.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.items.customContextMenuRequested.connect(lambda p: self.popmenu.exec(self.ui.items.mapToGlobal(p)))
        self.ui.items.itemSelectionChanged.connect(self._selection_changed)
        self.ui.items.dropEvent = self.dropEvent


# ----------------------------------------------------------------------------------------------------------------------
    def item(self) -> ItemModel:
        return self._list


# ----------------------------------------------------------------------------------------------------------------------
    def set_item_model(self, list: ItemModel):
        self._list = list
        for child in list.children:
            self.insert(child)


# ----------------------------------------------------------------------------------------------------------------------
    def update(self):
        for idx in range(self.ui.items.count()):
            widget: ChecklistWidget = self.ui.items.item(idx).data(QtCore.Qt.UserRole)
            widget.update()

        for idx in range(self.ui.children.count()):
            widget = self.ui.children.widget(idx)
            widget.update()


# ----------------------------------------------------------------------------------------------------------------------
    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        """When an item is dropped in the GUI, sort the parent list according to the GUI indexes.

        This feels like a hack.  Is there a better way to sync the GUI sort order to the model?
        """
        QtWidgets.QListWidget.dropEvent(self.ui.items, event)
        def get_index(item: ItemModel) -> int:
            for index in range(self.ui.items.count()):
                widget = self.ui.items.item(index)
                if widget.data(QtCore.Qt.UserRole).item() is item:
                    return index
            return None
        self._list.children.sort(key=get_index)


# ----------------------------------------------------------------------------------------------------------------------
    def _selection_changed(self):
        selected = self.ui.items.selectedIndexes()
        self.popmenu_delete.setEnabled(len(selected) == 1)
        if selected:
            row = selected[0].row()
            self.ui.children.setCurrentIndex(row)
            self.ui.children.setVisible(True)
            item = self.ui.items.item(row).data(QtCore.Qt.UserRole).item()
            self.itemSelected.emit(item)
        else:
            self.ui.children.setVisible(False)
            self.itemSelected.emit(None)


# ----------------------------------------------------------------------------------------------------------------------
    def get_selected_leaf_item(self) -> ChecklistItemWidget:
        """Dive the tree to get the child-most currently selected list widget."""
        selected = self.ui.items.selectedIndexes()
        if selected:
            index = selected[0].row()
            child: ChecklistWidget = self.ui.children.widget(index)
            item = child.get_selected_leaf_item()
            if item is None:
                item = self.ui.items.item(index).data(QtCore.Qt.UserRole)
            return item
        else:
            return None


# ----------------------------------------------------------------------------------------------------------------------
    def get_selected_leaf_list(self) -> 'ChecklistWidget':
        selected = self.ui.items.selectedIndexes()
        if selected:
            child: ChecklistWidget = self.ui.children.widget(selected[0].row())
            list = child.get_selected_leaf_list()
            if list is None:
                return child
            return list
        else:
            return self


# ----------------------------------------------------------------------------------------------------------------------
    def get_selected_leaf_parent_list(self) -> 'ChecklistWidget':
        selected = self.ui.items.selectedIndexes()
        if selected:
            child: ChecklistWidget = self.ui.children.widget(selected[0].row())
            list = child.get_selected_leaf_parent_list()
            if list is None:
                return self
            return list
        else:
            return None


# ----------------------------------------------------------------------------------------------------------------------
    def add(self):
        item = ItemModel(self._list)
        self._list.children.append(item)
        widget = self.insert(item)
        widget.edit()


# ----------------------------------------------------------------------------------------------------------------------
    def insert(self, item: ItemModel) -> ChecklistItemWidget:
        """Called to insert a new item into the list at the current selected location.

        If no item in the list is currently selected then insert a new item at the end of the list.
        """
        list_item = QtWidgets.QListWidgetItem(self.ui.items)
        list_item.setData(QtCore.Qt.UserRole, item)
        self.ui.items.addItem(list_item)
        item_widget = ChecklistItemWidget(None, item)
        list_item.setData(QtCore.Qt.UserRole, item_widget)
        self.ui.items.setItemWidget(list_item, item_widget)
        item_widget.contentChanged.connect(lambda: self.contentChanged.emit())

        # Recursively add children items to the children stack.
        list_widget = ChecklistWidget(self.ui.children)
        list_widget.set_item_model(item)
        list_widget.contentChanged.connect(lambda: self.contentChanged.emit())
        self.ui.children.addWidget(list_widget)

        return item_widget


# ----------------------------------------------------------------------------------------------------------------------
    def delete(self):
        """Fires to delete the currently selected item from the list."""
        selected = self.ui.items.selectedIndexes()
        if not selected:
            return
        row = selected[0].row()
        self.ui.items.takeItem(row)
        self.ui.children.removeWidget(self.ui.children.widget(row))
        self._list.children.pop(row)
        self.contentChanged.emit()




# End of File
