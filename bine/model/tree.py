# ======================================================================================================================
#      File:  /bine/model/tree.py
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
"""A document represents the root node in the tree and contains a title, description and tree of lists.

Inspiration for this model came from:
https://github.com/pyside/Examples/blob/master/examples/itemviews/editabletreemodel/editabletreemodel.py
"""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import pickle
import re
from turtle import pos
from typing import List, Union

from markdown import markdown
from PySide6 import QtCore, QtWidgets

from bine.model.item import TreeItem
from bine.settings import Settings




# ======================================================================================================================
# Tree Model Class
# ----------------------------------------------------------------------------------------------------------------------
class TreeModel(QtCore.QAbstractItemModel):

    def __init__(self, parent: QtWidgets.QTreeView = None):
        super().__init__(parent)

        self._title: str = ""
        self._description: str = ""
        self.root: TreeItem = TreeItem(text='root')
        self._cached = ''


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


# ----------------------------------------------------------------------------------------------------------------------
    def columnCount(self, parent = QtCore.QModelIndex()) -> int:
        return 1


# ----------------------------------------------------------------------------------------------------------------------
    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return None

        if role not in [QtCore.Qt.DisplayRole, QtCore.Qt.EditRole, QtCore.Qt.CheckStateRole]:
            return None

        item = self.getItem(index)
        return item.data(role)


# ----------------------------------------------------------------------------------------------------------------------
    def flags(self, index: QtCore.QModelIndex) -> QtCore.Qt.ItemFlags:
        if not index.isValid():
            return QtCore.Qt.ItemIsDropEnabled

        if index.column() != 0:
            return QtCore.Qt.NoItemFlags

        flags = QtCore.Qt.ItemIsEnabled
        flags |= QtCore.Qt.ItemIsSelectable
        flags |= QtCore.Qt.ItemIsEditable
        flags |= QtCore.Qt.ItemIsUserCheckable
        flags |= QtCore.Qt.ItemIsAutoTristate
        flags |= QtCore.Qt.ItemIsDragEnabled
        flags |= QtCore.Qt.ItemIsDropEnabled
        return flags


# ----------------------------------------------------------------------------------------------------------------------
    def mimeTypes(self) -> List[str]:
        return [
            'application/x-treeitemlist'
        ]


# ----------------------------------------------------------------------------------------------------------------------
    def mimeData(self, indexes: List[QtCore.QModelIndex]) -> QtCore.QMimeData:
        items = [self.getItem(index) for index in indexes]

        # Use the super's mimeData method to generate the QMimeData instance so that it's persistent.  Creating it
        # locally causes a crash when the garbage collector removes it upon return.
        data = super().mimeData(indexes)

        data.setText('\n'.join(item.text for item in items))
        data.setData('application/x-treeitemlist', pickle.dumps(items))

        return data


# ----------------------------------------------------------------------------------------------------------------------
    def supportedDropActions(self) -> QtCore.Qt.DropActions:
        return QtCore.Qt.MoveAction


# ----------------------------------------------------------------------------------------------------------------------
    def dropMimeData(self,
                     data: QtCore.QMimeData,
                     action: QtCore.Qt.DropAction,
                     row: int,
                     column: int,
                     parent: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]
                    ) -> bool:
        if not self.canDropMimeData(data, action, row, column, parent) or action == QtCore.Qt.IgnoreAction:
            return False

        if row > -1:
            position = row
        else:
            position = self.rowCount(parent if parent.isValid() else QtCore.QModelIndex())

        parent_item = self.getItem(parent)

        items: List[TreeItem] = pickle.loads(data.data('application/x-treeitemlist'))
        for item in items:

            # If this item is being moved up in the same parent list then adjust the insertion position.
            print(position, item.childNumber(), row, parent_item, item.parent)
            if item.childNumber() < position and parent_item == item.parent:
                position -= 1
                print('Decrement')

            self.removeItem(item)
            parent_item.insertChildren(position, 1)

            child_item = parent_item.child(position)
            child_item.setData(item.text, QtCore.Qt.EditRole)
            child_item.setData(item.checked, QtCore.Qt.CheckStateRole)

        self.dataChanged.emit(parent, parent)
        return True


# ----------------------------------------------------------------------------------------------------------------------
    def getItem(self, index: QtCore.QModelIndex) -> TreeItem:
        if index.isValid():
            item = index.internalPointer()
            if item:
                return item

        return self.root


# ----------------------------------------------------------------------------------------------------------------------
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole = QtCore.Qt.DisplayRole):
        # This model does not support headers.
        return None


# ----------------------------------------------------------------------------------------------------------------------
    def index(self, row: int, column: int, parent: QtCore.QModelIndex = QtCore.QModelIndex()):
        if parent.isValid() and parent.column() != 0:
            return QtCore.QModelIndex()

        parent_item = self.getItem(parent)
        childItem = parent_item.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()


# ----------------------------------------------------------------------------------------------------------------------
    def insertColumns(self, position: int, columns: int, parent: QtCore.QModelIndex = QtCore.QModelIndex()) -> bool:
        # This model only supports single columns - no additions or removals are supported.
        return False


# ----------------------------------------------------------------------------------------------------------------------
    def removeItem(self, item: TreeItem) -> bool:
        row = item.childNumber()
        print('Remove item', row, item.parent)
        index = self.createIndex(row, 0, item)
        return self.removeRows(row, 1, index.parent())


# ----------------------------------------------------------------------------------------------------------------------
    def insertRows(self, position: int, rows: int, parent=QtCore.QModelIndex()) -> bool:
        parent_item = self.getItem(parent)
        self.beginInsertRows(parent, position, position + rows - 1)
        success = parent_item.insertChildren(position, rows)
        self.endInsertRows()
        return success


# ----------------------------------------------------------------------------------------------------------------------
    def parent(self, index: QtCore.QModelIndex) -> QtCore.QModelIndex:
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = self.getItem(index)
        parent_item: TreeItem = childItem.parent

        if parent_item == self.root:
            return QtCore.QModelIndex()

        return self.createIndex(parent_item.childNumber(), 0, parent_item)


# ----------------------------------------------------------------------------------------------------------------------
    def removeColumns(self, position: int, columns: int, parent: QtCore.QModelIndex = QtCore.QModelIndex()) -> bool:
        # This model only supports exactly one column - additions and removals are not supported.
        return False


# ----------------------------------------------------------------------------------------------------------------------
    # def removeRows(self, position: int, rows: int, parent: QtCore.QModelIndex = QtCore.QModelIndex()) -> bool:
    #     parent_item: TreeItem = self.getItem(parent)

    #     self.beginRemoveRows(parent, position, position + rows - 1)
    #     success = parent_item.removeChildren(position, rows)
    #     print(f'Remove {rows} rows at {position} from {parent_item}')
    #     self.endRemoveRows()
    #     print(parent_item.children)

    #     return success


# ----------------------------------------------------------------------------------------------------------------------
    def rowCount(self, parent: QtCore.QModelIndex = QtCore.QModelIndex()) -> int:
        parent_item = self.getItem(parent)

        return parent_item.childCount()


# ----------------------------------------------------------------------------------------------------------------------
    def setData(self, index: QtCore.QModelIndex, value: TreeItem, role: QtCore.Qt.ItemDataRole = QtCore.Qt.EditRole) -> bool:
        if role not in [QtCore.Qt.EditRole, QtCore.Qt.CheckStateRole]:
            return False

        item = self.getItem(index)
        print('Set', item)
        result = item.setData(value, role)

        if result:
            self.dataChanged.emit(index, index)

        return result


# ----------------------------------------------------------------------------------------------------------------------
    def setHeaderData(self, section: int, orientation: QtCore.Qt.Orientation, value: TreeItem, role: QtCore.Qt.ItemDataRole = QtCore.Qt.EditRole) -> bool:
        # This model does not support headers.
        return False

# ----------------------------------------------------------------------------------------------------------------------
    def load(self, filename: str) -> None:
        """Load a document from file."""
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
        self.description, item_text = body.split('\n\n-', 1)
        item_text = '- ' + item_text.strip() + '\n'

        # Generate nested lists of Items from the list under the description.
        parents: List[TreeItem] = [self.root]
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
            parent.insertChildren(parent.childCount(), 1)
            item = parent.child(parent.childCount() - 1)
            item.setData(text, QtCore.Qt.DisplayRole)
            item.setData(QtCore.Qt.Checked if check_text != ' ' else QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)



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
        def dump_node(node: TreeItem) -> str:
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
    def _repr_recursion(self, item: TreeItem, indent: int = 0) -> str:
        result = " " * indent + repr(item) + "\n"
        for child in item.children:
            result += self._repr_recursion(child, indent + 2)
        return result


# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self) -> str:
        return self._repr_recursion(self.root)




# End of File
