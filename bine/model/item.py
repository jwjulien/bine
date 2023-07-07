# ======================================================================================================================
#      File:  /bine/model/item.py
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
"""A checklist contains Items (with checkboxes) and optionally more children Items."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from typing import List, Union

from PySide6 import QtCore, QtWidgets




# ======================================================================================================================
# Checklist Item Class
# ----------------------------------------------------------------------------------------------------------------------
class ChecklistItem:
    """Represents an "item" in the document tree containing checklist items with optional lists.

    Attributes:
        parent: Parent Checklist of this Checklist or None in the case of root list.
        text: Text for this item in the checklist.
        checked: Boolean indicating if this item is checked.  Calculated for non-leaf nodes.
        children: List of Items under this item - may be empty in the case of leaves.
    """
    def __init__(self, parent: 'ChecklistItem' = None, text: str = '', checked: bool = False):
        self.parent: 'ChecklistItem' = parent
        self.text: str = text
        self._checked: bool = checked
        self.children: List['ChecklistItem'] = []


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def checked(self):
        if not self.children:
            return self._checked
        # TODO: Can this be an option?  It's handy for some applications but there are circumstances when the parent
        # is better left unchecked until it is packed.  Like a duffel bag might be full, but not checked until loaded
        # into the car.
        return all([child.checked for child in self.children])

    @checked.setter
    def checked(self, value):
        self._checked = value


# ----------------------------------------------------------------------------------------------------------------------
    def clear(self) -> None:
        self.children = []


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def chain(self) -> List['ChecklistItem']:
        links = []
        if self.parent:
            links.extend(self.parent.chain)
        links.append(self)
        return links


# ----------------------------------------------------------------------------------------------------------------------
    def child(self, number: int) -> 'ChecklistItem':
        if number < 0 or number >= len(self.children):
            return None
        return self.children[number]


# ----------------------------------------------------------------------------------------------------------------------
    def childCount(self) -> int:
        return len(self.children)


# ----------------------------------------------------------------------------------------------------------------------
    def columnCount(self) -> int:
        # Checklist items specifically don't use columns - only one for the text of the item is supported.
        return 1


# ----------------------------------------------------------------------------------------------------------------------
    def row(self) -> int:
        """Get this item's row index.

        Returns:
            The zero-based row number of this item within it's parent's list of children.
        """
        # The root item is the only item without a parent and is singular, so always return 0.
        if self.parent is None:
            return 0

        return self.parent.children.index(self)


# ----------------------------------------------------------------------------------------------------------------------
    def isLastChild(self) -> bool:
        if self.parent is None:
            return False
        return self.row() == (len(self.parent.children) - 1)


# ----------------------------------------------------------------------------------------------------------------------
    def lastChild(self) -> 'ChecklistItem':
        return self.children[-1] if self.children else None


# ----------------------------------------------------------------------------------------------------------------------
    def data(self, column: int, role: QtCore.Qt.ItemDataRole) -> Union[str, int]:
        if role == QtCore.Qt.CheckStateRole:
            return int(QtCore.Qt.Checked if self.checked else QtCore.Qt.Unchecked)

        elif role in [QtCore.Qt.DisplayRole, QtCore.Qt.EditRole] and column == 0:
            return self.text

        return None


# ----------------------------------------------------------------------------------------------------------------------
    def setData(self,
                column: int,
                value: Union[str, QtCore.Qt.CheckState],
                role: QtCore.Qt.ItemDataRole
                ) -> bool:
        if role == QtCore.Qt.CheckStateRole:
            self.checked = value == QtCore.Qt.Checked
            return True

        if column == 0:
            self.text = value
            return True

        # No good - indicate that we didn't update anything.
        return False



# ----------------------------------------------------------------------------------------------------------------------
    def insertChildren(self, position: int, count: int, columns: int) -> bool:
        if position < 0 or position > len(self.children):
            return False

        # This specific model only supports one column for text.
        assert columns == 1

        for _ in range(count):
            item = ChecklistItem(self)
            self.children.insert(position, item)

        return True


# ----------------------------------------------------------------------------------------------------------------------
    def removeChildren(self, position: int, rows: int) -> bool:
        if position < 0 or (position + rows) > len(self.children):
            return False

        for _ in range(rows):
            self.children.pop(position)

        return True


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def level(self) -> int:
        if not self.parent:
            return 0
        return self.parent.level + 1


# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self) -> str:
        return f'<ChecklistItem at 0x{id(self):x} checked={self.checked} text="{self.text}">'





# End of File
