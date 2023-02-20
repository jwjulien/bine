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
from typing import List

from PySide6 import QtCore, QtGui, QtWidgets, QtPrintSupport

from bine.gui.base.tab import Ui_Tab
from bine.model.item import TreeItem
from bine.model.tree import TreeModel
from bine.libraries.undo.item import CommandItemEdit, CommandItemDelete, CommandItemInsert




# ======================================================================================================================
# Tab Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class TabWidget(QtWidgets.QWidget):
    """A tree and editor for a single document within a single tab of the GUI window."""

    contentChanged = QtCore.Signal()
    selectionChanged = QtCore.Signal(list)
    undoTextChanged = QtCore.Signal(str)
    redoTextChanged = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Tab()
        self.ui.setupUi(self)

        self.settings = parent.settings
        self.filename = None
        self.model = TreeModel(self.ui.tree)
        self.ui.tree.setModel(self.model)
        self.undo_stack = QtGui.QUndoStack(self)

        self._changed_from_insert = False

        self.ui.popmenu = QtWidgets.QMenu(self)
        self.ui.popmenu_insert_sibling = QtGui.QAction('Insert Sibling', self)
        self.ui.popmenu.addAction(self.ui.popmenu_insert_sibling)
        self.ui.popmenu_insert_child = QtGui.QAction('Insert Child', self)
        self.ui.popmenu.addAction(self.ui.popmenu_insert_child)
        self.ui.popmenu_delete = QtGui.QAction('Delete', self)
        self.ui.popmenu_delete.setEnabled(False)
        self.ui.popmenu.addAction(self.ui.popmenu_delete)
        self.ui.popmenu_insert_sibling.triggered.connect(self.insert_sibling)
        self.ui.popmenu_insert_child.triggered.connect(self.insert_child)
        self.ui.popmenu_delete.triggered.connect(self.delete)

        self.ui.tree.selectionModel().selectionChanged.connect(self.on_select)
        self.ui.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tree.customContextMenuRequested.connect(self.context)
        # self.ui.tree.dropEvent = self.dropped
        self.model.dataChanged.connect(lambda: self.contentChanged.emit())
        self.ui.title.textChanged.connect(self.title_changed)
        self.ui.description.textChanged.connect(self.description_changed)
        self.undo_stack.undoTextChanged.connect(lambda text: self.undoTextChanged.emit(text))
        self.undo_stack.redoTextChanged.connect(lambda text: self.redoTextChanged.emit(text))


# ----------------------------------------------------------------------------------------------------------------------
    def warn(self) -> bool:
        """Warn the user that there are unsaved changes and prompt them to save before continuing.

        Returns:
            True if the user has acknowledged the unsaved changes and processing should continue of False if the user
            has cancelled and the caller should cease what it was doing.
        """
        # No unsaved changes, nothing to warn about.
        if not self.model.dirty(self.settings):
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
    def open(self, filename: str):
        """Load the specified document in this tab.

        Arguments:
            filename: The path to the file to be loaded in this tab.
        """
        self.filename = filename
        self.model.load(self.filename)

        self.ui.title.setText(self.model.title)
        self.ui.description.setPlainText(self.model.description)
        self.ui.tree.setSelection(QtCore.QRect(0, 0, 1, 1), QtCore.QItemSelectionModel.ClearAndSelect)
        self.expand_all()

        self.contentChanged.emit()



# ----------------------------------------------------------------------------------------------------------------------
    def save(self) -> bool:
        """Called to save a currently open document to the opened filename.

        If no filename is set because this is a new document then revert to a "save as".

        Returns:
            Boolean True when the document is saved or False if the user cancelled out of the "save as" dialog.
        """
        if not self.filename:
            # If save was selected but this is a new document and filename hasn't been set then we need to pick a
            # filename now.
            return self.save_as()

        self.model.dump(self.filename, settings=self.settings, update_cache=True)
        self.contentChanged.emit()
        return True


# ----------------------------------------------------------------------------------------------------------------------
    def _save_dialog(self):
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
    def save_copy(self):
        """Save a copy of the current document and continue editing under the existing filename."""
        filename = self._save_dialog()
        if filename:
            self.model.dump(filename, self.settings, update_cache=False)


# ----------------------------------------------------------------------------------------------------------------------
    def on_select(self) -> List[TreeItem]:
        selections = self.ui.tree.selectedIndexes()
        items = [self.model.getItem(index) for index in selections]
        self.selectionChanged.emit(items)


# ----------------------------------------------------------------------------------------------------------------------
    def title_changed(self) -> None:
        self.model.title = self.ui.title.text()


# ----------------------------------------------------------------------------------------------------------------------
    def description_changed(self) -> None:
        """The user has modified the text in the editor window."""
        self.model.description = self.ui.description.toPlainText()


# ----------------------------------------------------------------------------------------------------------------------
    # def item_changed(self, node: QtWidgets.QTreeWidgetItem, _column: int):
    #     """Fires when the user modifies the item in the tree."""
        # item: TreeItem = node.data(0, QtCore.Qt.UserRole)
        # description = f'change item text from "{item.text}" to "{node.text(0)}"'
        # command = CommandItemEdit(self.ui.tree, node, item, description)
        # self.undo_stack.push(command)
        # if self._changed_from_insert:
        #     self.undo_stack.endMacro()
        #     self._changed_from_insert = False
        # item.text = node.text(0)
        # item.checked = node.checkState(0)
        # self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def undo(self):
        self.undo_stack.undo()
        self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def redo(self):
        self.undo_stack.redo()
        self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    # def dropped(self, event):
    #     """Called when an article in the tree is "dropped" from a resort event.

    #     Because the QTreeViewWidget does not automatically handle sorting updates for use we must hook this event and
    #     extract the new tree structure from the UI upon a drop.

    #     Arguments:
    #         event: The DropEvent object with info about what was dropped.
    #     """
    #     # Invoke the original parent function we are overriding.
    #     QtWidgets.QTreeWidget.dropEvent(self.ui.tree, event)

    #     def recurse(node: QtWidgets.QTreeWidgetItem, parent: TreeItem = None) -> List[TreeItem]:
    #         items = []
    #         count = node.childCount()
    #         if count > 0:
    #             for idx in range(count):
    #                 child = node.child(idx)
    #                 item: TreeItem = child.data(0, QtCore.Qt.UserRole)
    #                 item.parent = parent
    #                 item.children = recurse(child, item)
    #                 items.append(item)
    #         else:
    #             item = node.data(0, QtCore.Qt.UserRole)
    #             node.setCheckState(0, QtCore.Qt.Checked if item.checked else QtCore.Qt.Unchecked)
    #         return items

    #     # Reload the document structure from the tree.
    #     self.model.root.children = []
    #     for idx in range(self.ui.tree.topLevelItemCount()):
    #         node = self.ui.tree.topLevelItem(idx)
    #         item = node.data(0, QtCore.Qt.UserRole)
    #         item.parent = self.model.root
    #         item.children = recurse(node, item)
    #         self.model.root.children.append(item)

    #     self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def context(self, point: QtCore.QPoint):
        """Fires when the context menu is requested for the tree.

        Arguments:
            point: The location where the right click took place in the tree.
        """
        self.ui.popmenu.exec(self.ui.tree.mapToGlobal(point))


# ----------------------------------------------------------------------------------------------------------------------
    def insert_sibling(self):
        """Called to insert a new item into the tree at the selected location."""
        selection = self.ui.tree.selectedItems()
        new_item = TreeItem('', '')
        new_node = self._make_item(new_item)
        selected = None if not selection or not selection[-1].parent() else selection[-1]
        command = CommandItemInsert(self.ui.tree, new_node, selected, self.model.root, True)
        self.undo_stack.beginMacro('insert new sibling')
        self._changed_from_insert = True
        self.undo_stack.push(command)
        self.ui.tree.editItem(new_node, column=0)
        self.ui.tree.setCurrentItem(new_node, 0)
        self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def insert_child(self):
        """Called to insert a new item into the tree under the selected location."""
        selection = self.ui.tree.selectedItems()
        new_item = TreeItem('', '')
        new_node = self._make_item(new_item)
        selected = None if not selection else selection[-1]
        command = CommandItemInsert(self.ui.tree, new_node, selected, self.model.root, False)
        self.undo_stack.beginMacro('insert new child')
        self._changed_from_insert = True
        self.undo_stack.push(command)
        self.ui.tree.editItem(new_node, column=0)
        self.ui.tree.setCurrentItem(new_node, 0)
        self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def _selection(self, reverse: bool = False) -> List[QtWidgets.QListWidgetItem]:
        """Get a list of currently selected items, sorted by their index."""
        selection = self.ui.tree.selectedItems()
        def sort_by_index(node) -> int:
            if node.parent():
                return node.parent().indexOfChild(node)
            return self.ui.tree.indexOfTopLevelItem(node)
        selection.sort(key=sort_by_index, reverse=reverse)
        return selection


# ----------------------------------------------------------------------------------------------------------------------
    def delete(self):
        """Fires to delete the currently selected TreeItem from the tree."""
        selection = self._selection()
        if not selection:
            return
        for node in selection:
            command = CommandItemDelete(self.ui.tree, node)
            self.undo_stack.push(command)
        self.ui.tree.clearSelection()
        self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def move_up(self):
        """Fires when the user selects the move up menu option.  Moves the item up one position."""
        selection = self._selection()
        if not selection:
            return
        for node in selection:
            item: TreeItem = node.data(0, QtCore.Qt.UserRole)
            index = item.childNumber()
            if index > 0:
                item.parent.children.pop(index)
                item.parent.children.insert(index - 1, item)

                parent = node.parent()
                if parent:
                    parent.removeChild(node)
                    parent.insertChild(index - 1, node)
                else:
                    self.ui.tree.takeTopLevelItem(index)
                    self.ui.tree.insertTopLevelItem(index - 1, node)

                self.ui.tree.setCurrentItem(node, 0)

        self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def move_down(self):
        """Fires when the user selects the move down menu option.  Moves the item down one position."""
        selection = self._selection(True)
        if not selection:
            return
        for node in selection:
            item: TreeItem = node.data(0, QtCore.Qt.UserRole)
            index = item.childNumber()
            if index < (len(item.parent.children) - 1):
                item.parent.children.pop(index)
                item.parent.children.insert(index + 1, item)

                parent = node.parent()
                if parent:
                    parent.removeChild(node)
                    parent.insertChild(index + 1, node)
                else:
                    self.ui.tree.takeTopLevelItem(index)
                    self.ui.tree.insertTopLevelItem(index + 1, node)

                self.ui.tree.setCurrentItem(node, 0)

        self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def indent(self):
        """Fires when the user selects the indent menu option.  Moves the item to be a sibling of the item above."""
        selection = self._selection()
        if not selection:
            return
        top = selection[0]
        parent = top.parent()
        if parent:
            parent_item: TreeItem = parent.data(0, QtCore.Qt.UserRole)
            above = parent.child(parent.indexOfChild(top) - 1)
        else:
            parent_item: TreeItem = self.model.root
            above = self.ui.tree.topLevelItem(self.ui.tree.indexOfTopLevelItem(top) - 1)
        above_item: TreeItem = above.data(0, QtCore.Qt.UserRole)

        for node in selection:
            # Move the item in the model.
            item: TreeItem = node.data(0, QtCore.Qt.UserRole)
            parent_item.children.pop(item.childNumber())
            above_item.children.append(item)
            item.parent = above_item

            # Move the item in the tree.
            if parent:
                parent.removeChild(node)
            else:
                self.ui.tree.takeTopLevelItem(item.childNumber())
            above.addChild(node)

            self.ui.tree.setCurrentItem(node, 0)

        self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def dedent(self):
        """Fires when the user selects the dedent menu option.  Moves the selected item up to the parent level."""
        selection = self._selection(True)
        if not selection:
            return
        for node in selection:
            item: TreeItem = node.data(0, QtCore.Qt.UserRole)
            if item.parent.parent:
                # Move the node in the model.
                item.parent.children.pop(item.childNumber())
                index = item.parent.childNumber() + 1
                item.parent.parent.children.insert(index, item)
                item.parent = item.parent.parent

                # Move the node within the tree.
                parent = node.parent()
                parent.removeChild(node)

                if parent.childCount() == 0:
                    parent_item = parent.data(0, QtCore.Qt.UserRole)
                    parent.setCheckState(0, QtCore.Qt.Checked if parent_item.checked else QtCore.Qt.Unchecked)

                grandparent = parent.parent()
                if grandparent:
                    grandparent.insertChild(index, node)
                else:
                    self.ui.tree.insertTopLevelItem(index, node)

                self.ui.tree.setCurrentItem(node, 0)

        self.contentChanged.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def expand_all(self):
        """Expand all of the nodes in the tree."""
        self.ui.tree.expandAll()


# ----------------------------------------------------------------------------------------------------------------------
    def collapse_all(self):
        """Collapse all of the nodes in the tree."""
        self.ui.tree.collapseAll()


# ----------------------------------------------------------------------------------------------------------------------
    def on_print(self):
        """Print the current document."""
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec() == QtWidgets.QDialog.Accepted:
            browser = QtWidgets.QTextEdit()
            browser.setHtml(self.model.to_html())
            browser.print_(dialog.printer())


# ----------------------------------------------------------------------------------------------------------------------
    def preview(self):
        """Preview the HTML before printing."""
        browser = QtWidgets.QTextEdit()
        browser.setHtml(self.model.to_html(self.settings))
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
            document = self.model.to_html(self.settings)
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
