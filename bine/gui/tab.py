# ======================================================================================================================
#      File:  /bine/gui/tab.py
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
"""Tab container for a single document in the GUI."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import os
import pickle

from PySide6 import QtCore, QtGui, QtWidgets, QtPrintSupport

from bine.gui.base.tab import Ui_Tab
from bine.model.document import DocumentModel, ItemModel




# ======================================================================================================================
# Tab Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class TabWidget(QtWidgets.QWidget):
    """A tree and editor for a single document within a single tab of the GUI window."""

    contentChanged = QtCore.Signal()
    itemSelected = QtCore.Signal(ItemModel)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Tab()
        self.ui.setupUi(self)

        self.settings = parent.settings
        self.filename = None
        self.document = DocumentModel()
        self.clipboard = QtGui.QClipboard()

        # Connect events.
        self.ui.group.toggled.connect(self._toggle_details_group)

        # Connect the update event to the top level widget.  This way, any change from an item will update the state of
        # the entire tree.  This ensures that parents will update children when checked and progress bars get updated
        # for parents, going the other way.
        def item_changed():
            self.ui.lists.update()
            self.contentChanged.emit()
        self.ui.lists.contentChanged.connect(item_changed)
        self.ui.lists.itemSelected.connect(lambda item: self.itemSelected.emit(item))


# ----------------------------------------------------------------------------------------------------------------------
    def _toggle_details_group(self) -> None:
        if self.ui.group.isChecked():
            self.show_details()
        else:
            self.hide_details()


# ----------------------------------------------------------------------------------------------------------------------
    def show_details(self) -> None:
        self.ui.group.setChecked(True)
        self.ui.group.setFixedHeight(self.ui.group.sizeHint().height())


# ----------------------------------------------------------------------------------------------------------------------
    def hide_details(self) -> None:
        self.ui.group.setChecked(False)
        self.ui.group.setFixedHeight(18)


# ----------------------------------------------------------------------------------------------------------------------
    def open(self, filename: str) -> None:
        """Load the specified document in this tab.

        Arguments:
            filename: The path to the file to be loaded in this tab.
        """
        self.filename = filename
        self.document.load(self.filename)

        self.ui.title.setText(self.document.title)
        self.ui.description.setPlainText(self.document.description)
        self.ui.lists.set_item_model(self.document.root)

        # Hide the description if the document doesn't have one.
        if not self.document.description:
            self.hide_details()

        self.contentChanged.emit()



# ----------------------------------------------------------------------------------------------------------------------
    def save(self) -> bool:
        """Called to save a currently open document to the opened filename.

        If no filename is set because this is a new document then revert to a "save as".

        Returns:
            Boolean True when the document is saved or False if the user cancelled out of the "save as" dialog.
        """
        self.document.title = self.ui.title.text()
        self.document.description = self.ui.description.toPlainText()

        if not self.filename:
            # If save was selected but this is a new document and filename hasn't been set then we need to pick a
            # filename now.
            return self.save_as()

        self.document.dump(self.filename, settings=self.settings, update_cache=True)
        self.contentChanged.emit()
        return True


# ----------------------------------------------------------------------------------------------------------------------
    def _save_dialog(self) -> str:
        """Launch a save file dialog and return the selected filename.

        Shared for save as and save a copy.
        """
        filters = [
            'Markdown (*.md *.mkd *.mdwn *.mdown *.markdown *.mdtxt *.mdtext *.workbook)',
            'XML (*.xml)'
        ]
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, filter=';;'.join(filters))
        return filename


# ----------------------------------------------------------------------------------------------------------------------
    def save_as(self) -> bool:
        """Set a new filename for the document and save the contents into that.

        Returns:
            Boolean True when the document is saved or False if the user cancelled out of the "save as" dialog.
        """
        filename = self._save_dialog()
        if filename:
            self.filename = filename
            return self.save()
        return False


# ----------------------------------------------------------------------------------------------------------------------
    def save_copy(self) -> None:
        """Save a copy of the current document and continue editing under the existing filename."""
        filename = self._save_dialog()
        if filename:
            self.document.dump(filename, self.settings, update_cache=False)


# ----------------------------------------------------------------------------------------------------------------------
    def warn(self) -> bool:
        """Warn the user that there are unsaved changes and prompt them to save before continuing.

        Returns:
            True if the user has acknowledged the unsaved changes and processing should continue of False if the user
            has cancelled and the caller should cease what it was doing.
        """
        # No unsaved changes, nothing to warn about.
        if not self.document.dirty(self.settings):
            return True

        # Changes exist, lets prompt the user for an action.
        flags = QtWidgets.QMessageBox.Discard
        flags |= QtWidgets.QMessageBox.Save
        message = 'What would you like to do with your unsaved changes?'
        result = QtWidgets.QMessageBox.critical(self, 'Unsaved changes', message, flags)

        # If they sad "save" then lets try to save them.
        if result == QtWidgets.QMessageBox.Save:
            return self.save()

        # It they said discard then return True indicating the software should proceed anyways.
        return True


# ----------------------------------------------------------------------------------------------------------------------
    def copy(self) -> None:
        """Copy the currently selected item and it's children both as plain text and as binary (for internal use)."""
        widget = self.ui.lists.get_selected_leaf_item()
        if widget:
            item = widget.item()

            mime_data = QtCore.QMimeData()
            mime_data.setText(item.dump())
            mime_data.setData('application/vnd-bine-item', pickle.dumps(item))

            self.clipboard.setMimeData(mime_data)


# ----------------------------------------------------------------------------------------------------------------------
    def paste(self) -> None:
        mime_data = self.clipboard.mimeData()
        selected = self.ui.lists.get_selected_leaf_list()
        parent = selected.item()

        # First, see if there is any custom data to be pasted (copied to clipboard already from Bine).
        data = mime_data.data('application/vnd-bine-item')
        if data:
            try:
                item = pickle.loads(data)
            except pickle.UnpicklingError:
                return

            # Successfully unpickled - insert the item and correct the part/child double linkage.
            item.parent = parent
            parent.children.append(item)
            selected.insert(item)
            self.contentChanged.emit()

        # Otherwise, fall back on trying to do something with plain text.
        else:
            text = mime_data.text()
            if text:
                for text in text.split('\n'):
                    item = ItemModel(parent, text.strip())
                    parent.children.append(item)
                    selected.insert(item)
                self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def insert(self) -> None:
        selected = self.ui.lists.get_selected_leaf_list()
        selected.add()


# ----------------------------------------------------------------------------------------------------------------------
    def edit(self) -> None:
        selected = self.ui.lists.get_selected_leaf_item()
        if selected:
            selected.edit()


# ----------------------------------------------------------------------------------------------------------------------
    def delete(self) -> None:
        selected = self.ui.lists.get_selected_leaf_parent_list()
        if selected:
            selected.delete()


# ----------------------------------------------------------------------------------------------------------------------
    def toggle(self) -> None:
        selected = self.ui.lists.get_selected_leaf_item()
        if selected:
            selected.toggle()


# ----------------------------------------------------------------------------------------------------------------------
    def on_print(self) -> None:
        """Print the current document."""
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec() == QtWidgets.QDialog.Accepted:
            browser = QtWidgets.QTextEdit()
            browser.setHtml(self.document.to_html())
            browser.print_(dialog.printer())


# ----------------------------------------------------------------------------------------------------------------------
    def preview(self) -> None:
        """Preview the HTML before printing."""
        browser = QtWidgets.QTextEdit()
        browser.setHtml(self.document.to_html(self.settings))
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(browser.print_)
        dialog.exec()


# ----------------------------------------------------------------------------------------------------------------------
    def export_html(self, theme: str) -> None:
        """Export the current contents of the document to an HTML file.

        Arguments:
            theme: The name of the css theme to use in the generated HTML document ('white' or 'slate').
        """
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Export HTML', filter='HTML (*.html *.htm)')
        if filename:
            assets = os.path.join(os.path.dirname(__file__), '..', 'assets')
            def style(filename):
                with open(os.path.join(assets, 'css', filename), 'r', encoding='utf-8') as handle:
                    return f'<style type="text/css">{handle.read()}</style>'
            def script(filename):
                with open(os.path.join(assets, 'js', filename), 'r', encoding='utf-8') as handle:
                    return f'<script types="text/javascript">{handle.read()}</script>'
            document = self.document.to_html(self.settings)
            html = f"""<html>
    <head>
        {style('main.min.css')}
        {style('palette.min.css')}
        {script('palette.min.js')}
    </head>
    <body dir="ltr" data-md-color-scheme="{theme}">
        <div class="md-container">
            <main class="md-main">
                <div class="md-main__inner md-grid">
                    <div class="md-content">
                        <article class="md-content__inner md-typeset">
                           {document}
                        </article>
                    </div>
                </div>
            </main>
        </div>
    </body>
</html>"""

            with open(filename, 'w', encoding='utf-8') as handle:
                handle.write(html)




# End of File
