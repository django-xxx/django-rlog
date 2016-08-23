# -*- coding: utf-8 -*-

from django_rlog.connect import get_connection
from django_rlog.defaults import DEFAULT_KEY
from django_six import CompatibilityBaseCommand


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
        r = get_connection()
        r.rpush(options.get('key', DEFAULT_KEY), 'KILL')
