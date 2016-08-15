# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.management.base import BaseCommand


r = settings.REDIS_CACHE


DEFAULT_CHANNEL = 'django-logit'


class Command(BaseCommand):
    help = 'Stop rlog.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--channel',
            action='pubsub_channel',
            dest='pubsub_channel',
            default=DEFAULT_CHANNEL,
            help='Pubsub channel RedisHandler usage.',
        )

    def handle(self, *args, **options):
        r.publish(options.get('channel', DEFAULT_CHANNEL), 'KILL')
