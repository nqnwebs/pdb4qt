Set a tracepoint in the Python debugger that works with PyQt4

It uses ipdb_ if is available

Install
-------

From PyPI::

  $ pip install pdb4qt

Or by downloading the source and running::

  $ python setup.py install

Or, for the latest git version::

  $ pip install git+git://github.com/nqnwebs/pdb4qt.git


Usage
-----

Simply import ``set_trace`` from ``pdb4qt`` and call it where you want
to do the breakpoint::

    from pdb4qt import set_trace; set_trace()

Why it's needed?
----------------

Standard pdb/ipdb set_trace returns a loop of ``QCoreApplication::exec: The event loop is already running`` that disallow to input anything.

Credits
-------

It's heavily inspired on the answer of the user *quark* from
`this stackoverflow's thread <http://stackoverflow.com/questions/1736015/debugging-a-pyqt4-app>`_


.. _ipdb: http://pypi.python.org/pypi/ipdb
