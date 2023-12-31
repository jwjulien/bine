# ======================================================================================================================
#      File:  /bine/settings.py
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
"""Container for Bine's settings."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from dataclasses import dataclass




# ======================================================================================================================
# Settings Class
# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class Settings:
    highlight_duplicates: bool = True
    auto_check: bool = True
    auto_sort: bool = False
    hide_checked: bool = False

    # TODO: Add a load function to load these settings from file.
    # TODO: Add a save function to store these settings to file.




# ======================================================================================================================
# Settings Singleton
# ----------------------------------------------------------------------------------------------------------------------
settings = Settings()




# End of File
