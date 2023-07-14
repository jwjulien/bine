# ======================================================================================================================
#      File:  /bine/main.py
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
"""Main GUI application creation point."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import sys
import logging
from importlib import metadata
from argparse import ArgumentParser

from PySide6 import QtWidgets
import qdarktheme

from bine.gui.main import MainWindow




# ======================================================================================================================
# Main Function
# ----------------------------------------------------------------------------------------------------------------------
def main():
    # Setup command line inputs.
    parser = ArgumentParser(description=metadata.metadata('bine')['Summary'])
    parser.add_argument('files', nargs='*', help='optional file(s) to open in tabs')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='increase verbosity of terminal output')
    args = parser.parse_args()

    # Configure logging output.
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(2, args.verbose)]
    logging.basicConfig(level=level)

    # Setup GUI window.
    sys.argv += ['-platform', 'windows:darkmode=1']
    app = QtWidgets.QApplication(sys.argv)
    # qdarktheme.setup_theme('auto', 'sharp')
    window = MainWindow(args.files)
    window.show()

    # Run the app.
    return app.exec_()




# End of File
