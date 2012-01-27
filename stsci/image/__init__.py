from __future__ import division

from ._image import *
from .combine import *


try:
    from stsci.tools.version import (__version__, __svn_revision__,
                                     __svn_full_info__, __setup_datetime__)
except ImportError:
    __version__ = ''
    __svn_revision__ = ''
    __svn_full_info__ = ''
    __setup_datetime__ = None


try:
    import stsci.tools.tester
    def test(*args,**kwds):
        stsci.tools.tester.test(modname=__name__, *args, **kwds)
except ImportError:
    pass