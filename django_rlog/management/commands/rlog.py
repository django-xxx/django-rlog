# -*- coding: utf-8 -*-

from __future__ import print_function

from django.conf import settings
from django_rlog.defaults import DEFAULT_CHANNEL
from django_rlog.logger import get_logger
from django_rlog.management.commands._arguments import _add_arguments
from django_six import CompatibilityBaseCommand


r = settings.REDIS_CACHE


class Command(CompatibilityBaseCommand):
    help = "Save rlog's RedisHandler Log to Disk."

    def add_arguments(self, parser):
        parser.add_argument(
            '--channel',
            dest='channel',
            default=DEFAULT_CHANNEL,
            help='Pubsub channel RedisHandler use.',
        )
        _add_arguments(parser)

    def handle(self, *args, **options):
        debug = options.get('debug', False)
        logger = get_logger(**options)
        p = r.pubsub()
        p.subscribe(options.get('channel', DEFAULT_CHANNEL))
        for item in p.listen():
            if debug:
                print(item)
            p.unsubscribe() if item['data'] == 'KILL' else logger.debug(item.get('data', ''))
