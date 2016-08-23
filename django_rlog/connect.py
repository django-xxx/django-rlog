# -*- coding: utf-8 -*-

from django.conf import settings


def get_connection():
    for key in ['REDIS_CONN', 'REDIS_CLIENT', 'REDIS_CACHE']:
        if hasattr(settings, key):
            return getattr(settings, key)
