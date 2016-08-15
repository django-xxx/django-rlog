# -*- coding: utf-8 -*-

import logging
import logging.handlers

from django.conf import settings
from django_six import CompatibilityBaseCommand


r = settings.REDIS_CACHE


DEFAULT_CHANNEL = 'django-logit'
DEFAULT_FILENAME = '/tmp/django-logit.log'
DEFAULT_HANDLER = 'TimedRotatingFileHandler'
DEFAULT_WHEN = 'midnight'
DEFAULT_MAX_BYTES = 15728640,  # 1024 * 1024 * 15B = 15MB
DEFAULT_BACKUP_COUNT = 10


class Command(CompatibilityBaseCommand):
    help = "Save rlog's Pub/Sub Log to Disk."

    def add_arguments(self, parser):
        parser.add_argument(
            '--channel',
            dest='channel',
            default=DEFAULT_CHANNEL,
            help='Pubsub channel RedisHandler usage.',
        )
        parser.add_argument(
            '--filename',
            dest='filename',
            default=DEFAULT_FILENAME,
            help='Filename log write into.',
        )
        parser.add_argument(
            '--handler',
            dest='handler',
            default='FileHandler',
            help='FileHandler to use.',
        )
        parser.add_argument(
            '--when',
            dest='when',
            default=DEFAULT_WHEN,
            help='When of TimedRotatingFileHandler.',
        )
        parser.add_argument(
            '--maxBytes',
            dest='maxBytes',
            default=DEFAULT_MAX_BYTES,
            type=int,
            help='MaxBytes of RotatingFileHandler.',
        )
        parser.add_argument(
            '--backupCount',
            dest='backupCount',
            default=DEFAULT_BACKUP_COUNT,
            type=int,
            help='BackupCount of TimedRotatingFileHandler/RotatingFileHandler.',
        )

    def getHandler(self, **options):
        """Support FileHandler/RotatingFileHandler/TimedRotatingFileHandler"""
        filename = options.get('filename', DEFAULT_FILENAME)
        handler = options.get('handler', DEFAULT_FILENAME)
        when = options.get('when', DEFAULT_WHEN)
        maxBytes = options.get('maxBytes', DEFAULT_MAX_BYTES)
        backupCount = options.get('backupCount', DEFAULT_BACKUP_COUNT)

        if handler == 'TimedRotatingFileHandler':
            return logging.handlers.TimedRotatingFileHandler(filename, when=when, backupCount=backupCount)
        elif handler == 'RotatingFileHandler':
            return logging.handlers.RotatingFileHandler(filename, maxBytes=maxBytes, backupCount=backupCount)
        else:
            return logging.FileHandler(filename)

    def handle(self, *args, **options):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.getHandler(**options))
        p = r.pubsub()
        p.subscribe(options.get('channel', DEFAULT_CHANNEL))
        for item in p.listen():
            print item
            p.unsubscribe() if item['data'] == 'KILL' else logger.debug(item.get('data', ''))
