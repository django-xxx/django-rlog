# -*- coding: utf-8 -*-

import logging

from django.conf import settings
from django.core.management.base import BaseCommand


r = settings.REDIS_CACHE


DEFAULT_CHANNEL = 'django-logit'
DEFAULT_FILENAME = '/tmp/django-logit.log'


class Command(BaseCommand):
    help = "Save rlog's Pub/Sub Log to Disk."

    def add_arguments(self, parser):
        parser.add_argument(
            '--channel',
            action='pubsub_channel',
            dest='pubsub_channel',
            default=DEFAULT_CHANNEL,
            help='Pubsub channel RedisHandler usage.',
        )
        parser.add_argument(
            '--filename',
            action='filename',
            dest='filename',
            default=DEFAULT_FILENAME,
            help='Filename log write into.',
        )

    def handle(self, *args, **options):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(logging.FileHandler(options.get('filename', DEFAULT_FILENAME)))
        p = r.pubsub()
        p.subscribe(options.get('channel', DEFAULT_CHANNEL))
        for item in p.listen():
            print item
            p.unsubscribe() if item['data'] == 'KILL' else logger.debug(item.get('data', ''))
