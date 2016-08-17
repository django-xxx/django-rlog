# -*- coding: utf-8 -*-

from __future__ import print_function

from django.conf import settings
from django_rlog.defaults import DEFAULT_KEY, DEFAULT_TIMEOUT
from django_rlog.logger import get_logger
from django_rlog.management.commands._arguments import _add_arguments
from django_six import CompatibilityBaseCommand


r = settings.REDIS_CACHE


class Command(CompatibilityBaseCommand):
    help = "Save rlog's RedisListHandler Log to Disk."

    def add_arguments(self, parser):
        parser.add_argument(
            '--key',
            dest='key',
            default=DEFAULT_KEY,
            help='Key RedisListHandler use.',
        )
        parser.add_argument(
            '--timeout',
            dest='timeout',
            default=DEFAULT_TIMEOUT,
            type=int,
            help='Timeout of BLPOP/BRPOP.',
        )
        _add_arguments(parser)

    def handle(self, *args, **options):
        logger = get_logger(**options)
        key = options.get('key', DEFAULT_KEY)
        timeout = options.get('timeout', DEFAULT_TIMEOUT)
        while True:
            key, data = r.blpop(key, timeout)
            if data:
                print(data)
                logger.debug(data)
