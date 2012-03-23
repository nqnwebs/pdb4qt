#!/usr/bin/env python
# -*- coding: utf-8 -*-

def set_trace():
    '''
    Set a tracepoint in the Python debugger that works with Qt
    Taken from:
    http://stackoverflow.com/questions/1736015/debugging-a-pyqt4-app
    '''
    from PyQt4.QtCore import pyqtRemoveInputHook
    try:
        import ipdb as pdb
    except ImportError:
	import pdb
    pyqtRemoveInputHook()
    pdb.set_trace()
