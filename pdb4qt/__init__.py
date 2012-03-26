#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def set_trace(frame=None):
    '''
    Set a tracepoint in the Python debugger that works with Qt
    Taken from:
    http://stackoverflow.com/questions/1736015/debugging-a-pyqt4-app
    '''
    from PyQt4.QtCore import pyqtRemoveInputHook
    try:
        from ipdb import set_trace
    except ImportError:
        from pdb import set_trace
    pyqtRemoveInputHook()
    if frame is None:
        frame = sys._getframe().f_back
    return set_trace(frame)
