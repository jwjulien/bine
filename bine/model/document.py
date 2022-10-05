# ======================================================================================================================
#      File:  /bine/model/document.py
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
"""A document represents the root node in the tree and contains a title, description and tree of lists."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import re

from markdown import markdown

from bine.model.item import Item
from bine.settings import Settings




# ======================================================================================================================
# Document Class
# ----------------------------------------------------------------------------------------------------------------------
class Document:

    def __init__(self):
        super().__init__()
        self.title: str = ""
        self.description: str = ""
        self.root: Item = Item()
        self._cached = ''


# ----------------------------------------------------------------------------------------------------------------------
    def load(self, filename: str):
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
        previous_level = -1
        child = self.root
        parents = []
        items = re.split('^(\s*)-\s+\[(.)\]\s+(.+)\n', item_text, flags=re.MULTILINE)
        for indent, check_text, text in zip(items[1::4], items[2::4], items[3::4]):
            level = len(indent)
            while level > previous_level:
                parents.append(child)
                previous_level += 1
            while level < previous_level:
                parents.pop()
                previous_level -= 1
            parent = parents[-1]
            checked = check_text != ' '
            child = Item(parent, checked, text)
            parent.children.append(child)


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
        def dump_node(node: Item) -> str:
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
            'extra'
        ]
        html = markdown(text, extensions=extensions)
        return html


# ----------------------------------------------------------------------------------------------------------------------
    def clear(self):
        self.root.clear()
        self._cached = ''


# ----------------------------------------------------------------------------------------------------------------------
    def _repr_recursion(self, item: Item, indent: int = 0) -> str:
        result = " " * indent + repr(item) + "\n"
        for child in item.children:
            result += self._repr_recursion(child, indent + 2)
        return result


# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self) -> str:
        return self._repr_recursion(self.root)




# End of File
