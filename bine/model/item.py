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
from typing import List




# ======================================================================================================================
# Item Model
# ----------------------------------------------------------------------------------------------------------------------
class ItemModel:
    """Represents an "item" in the document tree containing checklist items with optional lists.

    Attributes:
        parent: Parent Checklist of this Checklist or None in the case of root list.
        text: Text for this item in the checklist.
        checked: Boolean indicating if this item is checked.  Calculated for non-leaf nodes.
        children: List of Items under this item - may be empty in the case of leaves.
    """
    def __init__(self, parent: 'ItemModel' = None, text: str = '', checked: bool = False):
        self.parent = parent
        self.text = text
        self._checked = checked
        self.children: List['ItemModel'] = []


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
        if self.children:
            for child in self.children:
                child.checked = value
        else:
            self._checked = value


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def chain(self) -> List['ItemModel']:
        if self.parent:
            return self.parent.chain + [self]
        return [self]


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def level(self) -> int:
        return len(self.chain) - 1


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def progress(self) -> int:
        """Return the percent completed of the children of this item on a scale of 0 to 100."""
        if not self.children:
            # Without children, the percentage is based upon the check state and it's all or nothing.
            return 100 if self.checked else 0

        # If this item has children then return the average.
        return sum([child.progress for child in self.children]) / len(self.children)



# ----------------------------------------------------------------------------------------------------------------------
    def clear(self) -> None:
        self.children = []
        self.text = ''
        self.checked = False


# ----------------------------------------------------------------------------------------------------------------------
    def dump(self, level: int = 0) -> str:
        indent = ' ' * (level * 4)
        text = f"{indent}- [{'x' if self.checked else ' '}] {self.text}\n"

        for child in self.children:
            text += child.dump(level + 1)

        return text


# ----------------------------------------------------------------------------------------------------------------------
    def repr(self, level: int = 1) -> str:
        indent = '  ' * level
        text = f"{indent}<ItemModel checked={self.checked} text=\"{self.text}\"{'/' if not self.children else ''}>"
        if self.children:
            text += '\n'
            text += f'\n'.join(child.repr(level + 1) for child in self.children)
            text += f'\n{indent}</ItemModel>'
        return text


# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self) -> str:
        return self.repr()




# End of File
