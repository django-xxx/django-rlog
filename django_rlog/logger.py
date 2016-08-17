# -*- coding: utf-8 -*-

import logging
import logging.handlers

from django_rlog.defaults import (DEFAULT_BACKUP_COUNT, DEFAULT_FILENAME, DEFAULT_HANDLER, DEFAULT_MAX_BYTES,
                                  DEFAULT_WHEN)


def get_handler(**options):
    """Support FileHandler/RotatingFileHandler/TimedRotatingFileHandler"""
    filename = options.get('filename', DEFAULT_FILENAME)
    handler = options.get('handler', DEFAULT_HANDLER)
    when = options.get('when', DEFAULT_WHEN)
    maxBytes = options.get('maxBytes', DEFAULT_MAX_BYTES)
    backupCount = options.get('backupCount', DEFAULT_BACKUP_COUNT)

    if handler == 'TimedRotatingFileHandler':
        return logging.handlers.TimedRotatingFileHandler(filename, when=when, backupCount=backupCount)
    elif handler == 'RotatingFileHandler':
        return logging.handlers.RotatingFileHandler(filename, maxBytes=maxBytes, backupCount=backupCount)
    else:
        return logging.FileHandler(filename)


def get_logger(**options):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_handler(**options))
    return logger
