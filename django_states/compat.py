# -*- coding: utf-8 -*-

from django.conf.urls import url, include

def curry(_curried_func, *args, **kwargs):
    def _curried(*moreargs, **morekwargs):
        return _curried_func(*args, *moreargs, **{**kwargs, **morekwargs})
    return _curried
