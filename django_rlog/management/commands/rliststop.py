# -*- coding: utf-8 -*-

from django.conf import settings
from django_rlog.defaults import DEFAULT_KEY
from django_six import CompatibilityBaseCommand


r = settings.REDIS_CACHE


class Command(CompatibilityBaseCommand):
    help = 'Stop rlistlog.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--key',
            dest='key',
            default=DEFAULT_KEY,
            help='Key RedisListHandler use.',
        )

    def handle(self, *args, **options):
        r.rpush(options.get('key', DEFAULT_KEY), 'KILL')
