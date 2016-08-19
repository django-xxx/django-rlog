# -*- coding: utf-8 -*-

from django_rlog.defaults import (DEFAULT_BACKUP_COUNT, DEFAULT_FILENAME, DEFAULT_HANDLER, DEFAULT_MAX_BYTES,
                                  DEFAULT_WHEN)


def _add_arguments(parser):
    """Add Common Arguments"""
    parser.add_argument(
        '--filename',
        dest='filename',
        default=DEFAULT_FILENAME,
        help='Filename log write into.',
    )
    parser.add_argument(
        '--handler',
        dest='handler',
        default=DEFAULT_HANDLER,
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
    parser.add_argument(
        '--debug',
        action='store_true',
        dest='debug',
        default=False,
        help='Print info or not.',
    )
