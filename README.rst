===========
django-rlog
===========

Save rlog's Pub/Sub Log to Disk

Installation
============

::

    pip install django-rlog


Usage
=====

Start rlog::

    python manage.py rlog [channel] [filename] [handler] [when] [maxBytes] [backupCount]


Start rlistlog::

    python manage.py rlistlog [key] [timeout] [filename] [handler] [when] [maxBytes] [backupCount]


Stop rlog::

    python manage.py rstop [channel]

