# -*- coding: utf-8 -*-

from django_rlog.connect import get_connection
from django_rlog.defaults import DEFAULT_CHANNEL
from django_six import CompatibilityBaseCommand


class Command(CompatibilityBaseCommand):
    help = 'Stop rlog.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--channel',
            dest='channel',
            default=DEFAULT_CHANNEL,
            help='Pubsub channel RedisHandler usage.',
        )

    def handle(self, *args, **options):
        r = get_connection()
        r.publish(options.get('channel', DEFAULT_CHANNEL), 'KILL')
