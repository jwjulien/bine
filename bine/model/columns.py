# ======================================================================================================================
#      File:  /bine/model/columns.py
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
"""A hierarchial model of items to represent a tree structure for Qt views.

Heavy inspiration for this model was taken from:
https://felgo.com/doc/qt/qtwidgets-itemviews-simpletreemodel-example/#treemodel-class-implementation
"""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import pickle
import re
from typing import List, Union

from markdown import markdown
from PySide6 import QtCore, QtWidgets

from bine.settings import Settings
from bine.model.item import ChecklistItem




# ======================================================================================================================
# Columns Model Class
# ----------------------------------------------------------------------------------------------------------------------
class ColumnsModel(QtCore.QAbstractItemModel):

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)

        self._title: str = ""
        self._description: str = ""

        self.root: ChecklistItem = ChecklistItem(text='root')

        self._cached = ''



# ======================================================================================================================
# Getters/Setters for high-level properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value != self._description:
            self._description = value
            self.dataChanged.emit(None, None)


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value != self._title:
            self._title = value
            self.dataChanged.emit(None, None)



# ======================================================================================================================
# "Special" Methods? - Not really sure what best to call these methods, they don't fall into a single category below.
# ----------------------------------------------------------------------------------------------------------------------
    def flags(self, index: QtCore.QModelIndex) -> QtCore.Qt.ItemFlags:
        if not index.isValid():
            return QtCore.Qt.NoItemFlags

        flags = QtCore.Qt.ItemIsEnabled
        flags |= QtCore.Qt.ItemIsSelectable
        flags |= QtCore.Qt.ItemIsEditable
        flags |= QtCore.Qt.ItemIsUserCheckable
        flags |= QtCore.Qt.ItemIsAutoTristate
        # flags |= QtCore.Qt.ItemIsDragEnabled
        # flags |= QtCore.Qt.ItemIsDropEnabled
        return flags



# ======================================================================================================================
# Methods for Reading TreeModel
# ----------------------------------------------------------------------------------------------------------------------
    def item(self, index: QtCore.QModelIndex) -> ChecklistItem:
        """Get the item from the provided index.

        Valid indexes *should* have ChecklistItems attached to their internalPointer's, but this method will verify that
        the index is valid and that the internalPointer is too.

        Arguments:
            index: A QModelIndex that refers to a ChecklistItem.

        Returns:
            The ChecklistItem from the provided `index`, or the root ChecklistItem in the event that the `index` is
            invalid.
        """
        if index is not None and index.isValid():
            item = index.internalPointer()
            if item:
                return item

        return self.root


# ----------------------------------------------------------------------------------------------------------------------
    def index(self,
              row: int,
              column: int,
              parent_index: QtCore.QModelIndex = QtCore.QModelIndex()
              ) -> QtCore.QModelIndex:
        """Get the index for the item at the specified location under the provided parent.

        Arguments:
            row: Integer row number of the child item of interest.
            column: Integer column number of the child item of interest.
            parent_index: QModelIndex of the parent item for this item.

        Returns:
            QModelIndex for the specified item.
        """
        # Return an invalid index of the provided values are not contained in this model.
        if not self.hasIndex(row, column, parent_index):
            return QtCore.QModelIndex()

        # Determine the parent item for this index based upon the provided parent index.
        parent_item = self.item(parent_index)

        # Fetch the child corresponding to the provided row.
        child_item = parent_item.child(row)
        if child_item:
            return self.createIndex(row, column, child_item)

        # This shouldn't really happen, but if there is no corresponding child then return an invalid index.
        return QtCore.QModelIndex()


# ----------------------------------------------------------------------------------------------------------------------
    def root_index(self) -> QtCore.QModelIndex:
        """Special method that returns the index of the root.

        Devised to allow appending items to the root list when no selections are valid.

        Returns:
            A QModelIndex for the end of the root list.
        """
        return self.createIndex(self.root.childCount(), 0, self.root)


# ----------------------------------------------------------------------------------------------------------------------
    def parent(self, child_index: QtCore.QModelIndex) -> QtCore.QModelIndex:
        if not child_index.isValid():
            return QtCore.QModelIndex()

        # Get the item that corresponds with the provided child index.
        child_item: ChecklistItem = self.item(child_index)

        # Extract the parent item from that child item.
        parent_item: ChecklistItem = child_item.parent

        # Return an invalid index for the root item - we do not want to display it.
        if parent_item is None or parent_item == self.root:
            return QtCore.QModelIndex()

        # If all is good, return an index for the parent item.
        return self.createIndex(parent_item.row(), 0, parent_item)


# ----------------------------------------------------------------------------------------------------------------------
    def rowCount(self, parent_index: QtCore.QModelIndex = QtCore.QModelIndex()) -> int:
        """Get the number of rows associated with an index.

        Arguments:
            parent_index: The QModelIndex of the parent containing child items.

        Returns:
            The integer number of rows (i.e. children) associated with the provided index or the number of top level
            items directly under the root node if the provided index is invalid.
        """
        # If being asked for the row cound on anything other than column 0 then the answer is always zero.
        if parent_index.isValid() and parent_index.column() > 0:
            return 0

        # Grab the item from the index and return the number of children associated with it.
        parent_item: ChecklistItem = self.item(parent_index)
        return parent_item.childCount()


# ----------------------------------------------------------------------------------------------------------------------
    def columnCount(self, parent_index = None) -> int:
        parent_item: ChecklistItem = self.item(parent_index)
        return parent_item.columnCount()


# ----------------------------------------------------------------------------------------------------------------------
    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole) -> Union[int, str]:
        if not index.isValid():
            return None

        item: ChecklistItem = self.item(index)
        return item.data(index.column(), role)


# ----------------------------------------------------------------------------------------------------------------------
    def headerData(self,
                   section: int,
                   orientation: QtCore.Qt.Orientation,
                   role: QtCore.Qt.ItemDataRole = QtCore.Qt.DisplayRole
                   ) -> str:
        # This model does not currently support headers.
        return None

        # TODO: Can we make this some kind of option to make this model more flexible?
        # if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
        #     return self.root.data(section)




# ======================================================================================================================
# Methods for Editing The TreeModel
# ----------------------------------------------------------------------------------------------------------------------
    def setData(self,
                index: QtCore.QModelIndex,
                value: Union[str, QtCore.Qt.CheckState],
                role: QtCore.Qt.ItemDataRole = QtCore.Qt.EditRole
                ) -> bool:

        item: ChecklistItem = self.item(index)
        success: bool = item.setData(index.column(), value, role)

        if success:
            print('Set', item)
            self.dataChanged.emit(index, index)

        return success


# ----------------------------------------------------------------------------------------------------------------------
    def setHeaderData(self,
                      section: int,
                      orientation: QtCore.Qt.Orientation,
                      value: ChecklistItem,
                      role: QtCore.Qt.ItemDataRole = QtCore.Qt.EditRole
                      ) -> bool:
        # This model currently doesn't support headers so there's nothing to do here.
        # TODO: If we add support for headers then this will also be needed.
        return False


# ----------------------------------------------------------------------------------------------------------------------
    def insertColumns(self, position: int, columns: int, parent: QtCore.QModelIndex = QtCore.QModelIndex()) -> bool:
        # This model currently only supports single columns - no additions or removals are supported.
        return False


# ----------------------------------------------------------------------------------------------------------------------
    def removeColumns(self, position: int, columns: int, parent: QtCore.QModelIndex = QtCore.QModelIndex()) -> bool:
        # This model currently only supports exactly one column - additions and removals are not supported.
        return False


# ----------------------------------------------------------------------------------------------------------------------
    def insertRows(self, position: int, rows: int, parent: QtCore.QModelIndex = QtCore.QModelIndex()) -> bool:
        parent_item = self.item(parent)
        self.beginInsertRows(parent, position, position + rows - 1)
        success = parent_item.insertChildren(position, rows, 1)
        self.endInsertRows()
        return success


# ----------------------------------------------------------------------------------------------------------------------
    def removeRows(self, position: int, rows: int, parent: QtCore.QModelIndex = QtCore.QModelIndex()) -> bool:
        parent_item: ChecklistItem = self.item(parent)

        self.beginRemoveRows(parent, position, position + rows - 1)
        success = parent_item.removeChildren(position, rows)
        print(f'Remove {rows} rows at {position} from {parent_item}')
        self.endRemoveRows()
        print(parent_item.children)

        return success












# ======================================================================================================================
# !?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?
# ----------------------------------------------------------------------------------------------------------------------


















# ----------------------------------------------------------------------------------------------------------------------
#     def mimeTypes(self) -> List[str]:
#         return [
#             'application/x-treeitemlist'
#         ]


# # ----------------------------------------------------------------------------------------------------------------------
#     def mimeData(self, indexes: List[QtCore.QModelIndex]) -> QtCore.QMimeData:
#         items = [self.item(index) for index in indexes]

#         # Use the super's mimeData method to generate the QMimeData instance so that it's persistent.  Creating it
#         # locally causes a crash when the garbage collector removes it upon return.
#         data = super().mimeData(indexes)

#         data.setText('\n'.join(item.text for item in items))
#         data.setData('application/x-treeitemlist', pickle.dumps(items))

#         return data


# # ----------------------------------------------------------------------------------------------------------------------
#     def supportedDropActions(self) -> QtCore.Qt.DropActions:
#         return QtCore.Qt.MoveAction


# # ----------------------------------------------------------------------------------------------------------------------
#     def dropMimeData(self,
#                      data: QtCore.QMimeData,
#                      action: QtCore.Qt.DropAction,
#                      row: int,
#                      column: int,
#                      parent: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]
#                     ) -> bool:
#         if not self.canDropMimeData(data, action, row, column, parent) or action == QtCore.Qt.IgnoreAction:
#             return False

#         if row > -1:
#             position = row
#         else:
#             position = self.rowCount(parent if parent.isValid() else QtCore.QModelIndex())

#         parent_item = self.item(parent)

#         items: List[ChecklistItem] = pickle.loads(data.data('application/x-treeitemlist'))
#         for item in items:

#             # If this item is being moved up in the same parent list then adjust the insertion position.
#             print(position, item.row(), row, parent_item, item.parent)
#             if item.row() < position and parent_item == item.parent:
#                 position -= 1
#                 print('Decrement')

#             self.removeItem(item)
#             parent_item.insertChildren(position, 1)

#             child_item = parent_item.child(position)
#             child_item.setData(0, item.text, QtCore.Qt.EditRole)
#             child_item.setData(0, item.checked, QtCore.Qt.CheckStateRole)

#         self.dataChanged.emit(parent, parent)
#         return True


# # ----------------------------------------------------------------------------------------------------------------------
#     def removeItem(self, item: ChecklistItem) -> bool:
#         row = item.row()
#         print('Remove item', row, item.parent)
#         index = self.createIndex(row, 0, item)
#         return self.removeRows(row, 1, index.parent())

# ----------------------------------------------------------------------------------------------------------------------
    def load(self, filename: str) -> None:
        """Load a document from file."""
        self.beginResetModel()
        with open(filename, 'r', encoding='utf-8') as handle:
            document = handle.read()

        self._cached = document

        # Convert underline headings to pound headings.
        document = re.sub('(.+)\n===+\n', r'# \1\n', document)
        document = re.sub('(.+)\n---+\n', r'## \1\n', document)

        # Ensure that the document ends with a newline.
        document += '\n'

        # Parse out sections using headings as titles.
        sections = re.split('^#+\s*', document, flags=re.MULTILINE)[1:]
        if len(sections) != 1:
            raise ValueError('Provided file does not follow expected checklist conventions.')
        self.title, body = sections[0].split('\n', 1)
        try:
            self.description, item_text = body.split('\n\n-', 1)
        except ValueError:
            # A ValueError is thrown if the double-newline fails to match, indicating there is no description in this
            # file.
            self.description = ''
            item_text = body
        item_text = '- ' + item_text.strip() + '\n'

        # Generate nested lists of Items from the list under the description.
        parents: List[ChecklistItem] = [self.root]
        indentations = [0]
        items = re.split('^(\s*)-\s+\[(.)\]\s+(.+)\n', item_text, flags=re.MULTILINE)
        for leader, check_text, text in zip(items[1::4], items[2::4], items[3::4]):
            indent = len(leader)
            if indent > indentations[-1]:
                if parents[-1].childCount() > 0:
                    parents.append(parents[-1].child(parents[-1].childCount() - 1))
                    indentations.append(indent)
            else:
                while indent < indentations[-1] and len(parents) > 0:
                    parents.pop()
                    indentations.pop()
            parent = parents[-1]
            checked = bool(check_text != ' ')
            self.insertItem(parent, text, checked)

        # self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.root.childCount(), 0))
        self.endResetModel()


# ----------------------------------------------------------------------------------------------------------------------
    def insertItem(self, parent: ChecklistItem, text: str = '', checked: bool = False) -> QtCore.QModelIndex:
        row = parent.childCount()
        index = self.createIndex(row, 0)
        self.beginInsertRows(index, row, row)
        parent.insertChildren(row, 1, 1)
        item = parent.child(row)
        item.setData(0, text, QtCore.Qt.DisplayRole)
        item.setData(0, QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
        self.endInsertRows()
        return index


# ----------------------------------------------------------------------------------------------------------------------
    def dump(self, filename: str, settings: Settings, update_cache: bool) -> None:
        """Write the contents of this model to the provided filename.

        Arguments:
            filename: The path and name of the file to which the contents of this Document are to be dumped.
            headings: The format to use for the headings in the output file.
        """
        document = self.dumps(settings)
        with open(filename, 'w', encoding='utf-8') as handle:
            handle.write(document)
        if update_cache:
            self._cached = document


# ----------------------------------------------------------------------------------------------------------------------
    def dumps(self, settings: Settings) -> str:
        """Return the contents of this document as a sting."""
        def dump_node(node: ChecklistItem) -> str:
            text = ''

            for item in node.children:
                indent = ' ' * ((item.level - 1) * 4)
                text += f"{indent}- [{'x' if item.checked else ' '}] {item.text}\n"

                # Recurse into children, when applicable (returns nothing when this is a leaf node).
                text += dump_node(item)

            return text

        text = self.title + '\n'
        text += ('=' * 120) + '\n'
        text += self.description
        text += '\n\n'
        text += dump_node(self.root)
        return text


# ----------------------------------------------------------------------------------------------------------------------
    def dirty(self, settings: Settings) -> bool:
        current = self.dumps(settings)
        return current != self._cached


# ----------------------------------------------------------------------------------------------------------------------
    def to_html(self, settings: Settings) -> str:
        text = self.dumps(settings)
        extensions = [
            'admonition',
            'codehilite',
            'extra',
            'pymdownx.tasklist'
        ]
        html = markdown(text, extensions=extensions)
        return html


# ----------------------------------------------------------------------------------------------------------------------
    def clear(self):
        self.root.clear()
        self._cached = ''


# ----------------------------------------------------------------------------------------------------------------------
    def _repr_recursion(self, item: ChecklistItem, indent: int = 0) -> str:
        result = " " * indent + repr(item) + "\n"
        for child in item.children:
            result += self._repr_recursion(child, indent + 2)
        return result


# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self) -> str:
        return self._repr_recursion(self.root)




# End of File
