# -*- coding: utf-8 -*-

from django.conf import settings
from django_six import CompatibilityBaseCommand


r = settings.REDIS_CACHE


DEFAULT_CHANNEL = 'django-logit'


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
        r.publish(options.get('channel', DEFAULT_CHANNEL), 'KILL')
