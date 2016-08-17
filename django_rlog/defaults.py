# -*- coding: utf-8 -*-

# Default Channel RedisHandler Use
DEFAULT_CHANNEL = 'django-logit'

# Default Key RedisListHandler Use
DEFAULT_KEY = 'django:logit'

# Default Timeout for BLPOP/BRPOP
DEFAULT_TIMEOUT = 60

# Default Filename Logs Write Into
DEFAULT_FILENAME = '/tmp/django-logit.log'

# Default Handler Logger Use
DEFAULT_HANDLER = 'TimedRotatingFileHandler'

# Default When for TimedRotatingFileHandler
DEFAULT_WHEN = 'midnight'

# Default MaxBytes for RotatingFileHandler
DEFAULT_MAX_BYTES = 15728640  # 1024 * 1024 * 15B = 15MB

# Default Backup Count for TimedRotatingFileHandler/RotatingFileHandler
DEFAULT_BACKUP_COUNT = 10
