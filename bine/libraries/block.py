# ======================================================================================================================
#      File:  /bine/libraries/block.py
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
"""A simple lockout mechanism to assist with blocking GUI updates in loops."""

# ======================================================================================================================
# Exceptions
# ----------------------------------------------------------------------------------------------------------------------
class UnbalancedBlock(Exception):
    """Raised when an unlock is attempted before the corresponding lock request."""



# ======================================================================================================================
# Block Class
# ----------------------------------------------------------------------------------------------------------------------
class Block:
    """A blocking mechanism to prevent certain tasks from running under conditions.

    Originally developed to prevent GUI updates from cyclicly triggering updates due to connected signals.  A Block.lock
    in one method, before the update, prevents new signals from being emitted in another method until the Block.unlock
    request.

    Also works with the Python context manager:

        block = Block()
        with block:
            do.a.thing()

    Properties:
        locked: Bool indicating that this block is currently locked out.
        unlocked: Polar opposite of the `locked` property, for convenience.
    """
    def __init__(self):
        self._counter = 0


    def __enter__(self):
        self.lock()

    def __exit__(self, type, value, traceback):
        self.unlock()


    def lock(self) -> None:
        """Lock the block."""
        self._counter += 1

    def unlock(self) -> None:
        """Unlock the block."""
        if self._counter > 0:
            self._counter -= 1
        else:
            raise UnbalancedBlock('Unlock attempt without matching lock request.')


    @property
    def locked(self) -> bool:
        return self._counter > 0

    @property
    def unlocked(self) -> bool:
        return not self.locked




# End of File
