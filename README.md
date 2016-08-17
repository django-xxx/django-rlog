# django-six
Save rlog's Pub/Sub Log to Disk

## Installation
```
pip install django-rlog
```

## Usage
* Start rlog
```shell
python manage.py rlog [channel] [filename] [handler] [when] [maxBytes] [backupCount]
```
* Start rlistlog
```shell
python manage.py rlistlog [key] [timeout] [filename] [handler] [when] [maxBytes] [backupCount]
```
* Stop rlog
```shell
python manage.py rstop [channel]
```
