# django-six
Save rlog's Pub/Sub Log to Disk

## Installation
```
pip install django-rlog
```

## Usage
* Start rlog
```shell
python manage.py rlog [channel] [filename] [handler] [when] [maxBytes] [backupCount] [debug]
```
* Start rlistlog
```shell
python manage.py rlistlog [key] [timeout] [filename] [handler] [when] [maxBytes] [backupCount] [debug]
```
* Stop rlog
```shell
python manage.py rstop [channel]
```
* Stop rlistlog
```shell
python manage.py rliststop [key]
```

## Redis Connection
```python
def get_connection():
    for key in ['REDIS_CONN', 'REDIS_CLIENT', 'REDIS_CACHE']:
        if hasattr(settings, key):
            return getattr(settings, key)
```
  * Get ``Redis Connection`` from settings
  * ``Redis Connection`` in settings refer to [Django Cook Book](https://github.com/xxx-cook-book/django-cook-book/tree/master/Caches/Redis)
