# -*- coding: utf-8 -*-
"""
State engine for django models.

Define a state graph for a model and remember the state of each object.
State transitions can be logged for objects.
"""
from __future__ import absolute_import
from six.moves import map

#: The version list
VERSION = (1, 6, 4)

#: The actual version number, used by python (and shown in sentry)
__version__ = '.'.join(map(str, VERSION))
