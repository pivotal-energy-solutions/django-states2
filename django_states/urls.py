# -*- coding: utf-8 -*-
"""Urls"""
from __future__ import absolute_import

from django.urls import path

from django_states.views import make_state_transition

urlpatterns = [
    path('make-state-transition/', make_state_transition, name='django_states_make_transition'),
]
