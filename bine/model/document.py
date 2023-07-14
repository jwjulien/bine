# ======================================================================================================================
#      File:  /bine/model/document.py
#   Project:  Bine
#    Author:  Jared Julien <jaredjulien@exsystems.net>
# Copyright:  (c) 2023 Jared Julien, eX Systems
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
"""A Document represents a single Markdown file containing a title, optional description, and a set of checklists."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import re
from typing import List

import markdown

from bine.model.item import ItemModel
from bine.settings import Settings




# ======================================================================================================================
# Document Model
# ----------------------------------------------------------------------------------------------------------------------
class DocumentModel:
    """A Document is the top-level Markdown file representation of a checklist."""

    def __init__(self):
        self.title: str = ""
        self.description: str = ""

        self.root: ItemModel = ItemModel(None, 'root')

        self._cached = ''



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
        try:
            self.description, item_text = body.split('\n\n-', 1)
        except ValueError:
            # A ValueError is thrown if no description was provided - default to empty string.
            self.description = ''
            item_text = body
        else:
            # The leading dash and trailing newline got stripped by re, hack them back for the parsing below.
            item_text = '- ' + item_text.strip() + '\n'

        # Generate nested List of Items from the list under the description.
        parents: List[ItemModel] = [self.root]
        indentations = [0]
        items = re.split('^([ \t]*)[-*][ \t]*(?:\[(.)\])?[ \t]*(.*?)$', item_text, flags=re.MULTILINE)
        for leader, check_text, text in zip(items[1::4], items[2::4], items[3::4]):
            indent = len(leader)

            # Skip empty items.
            if not text:
                continue

            # Decide if we need to change levels.
            if indent > indentations[-1]:
                # Indent increased, we are looking at a new child.
                children = len(parents[-1].children)
                if children > 0:
                    # Push the last item added into the part stack.
                    parents.append(parents[-1].children[children - 1])
                    # Adjust the indentation to show the new level.
                    indentations.append(indent)
            else:
                # We are moving out of a child - could be more than one step though.
                while indent < indentations[-1] and len(parents) > 0:
                    # For each step, pop a parent off the stack.
                    parents.pop()
                    indentations.pop()

            # With that sorted, the parent for this list will be the one at the end of the parents stack.
            parent = parents[-1]

            # Insert the item.
            checked = bool(check_text is not None and check_text != ' ')
            parent.children.append(ItemModel(parent, text, checked))



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
        text = self.title + '\n'
        text += ('=' * 120) + '\n'
        if self.description:
            text += self.description
            text += '\n\n'
        for child in self.root.children:
            text += child.dump()
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
    def __repr__(self) -> str:
        description = self.description.replace('\n', '\\n')
        text = f'<Document title="{self.title} description="{description}">\n'
        text += '\n'.join(item.repr() for item in self.root.children)
        text += '\n</Document>'
        return text




# End of File
