# -*- coding: utf-8 -*-
"""Urls"""

from django.urls import re_path
from django_states.views import make_state_transition

urlpatterns = [
    re_path(r'^make-state-transition/$', make_state_transition,
            name='django_states_make_transition'),
]
