"""Signals"""

import django.dispatch

#: Signal that is sent before a state transition is executed
before_state_execute = django.dispatch.Signal()
#: Signal that s sent after a state transition is executed
after_state_execute = django.dispatch.Signal()
