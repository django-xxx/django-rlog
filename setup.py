# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.5'


setup(
    name='django-rlog',
    version=version,
    keywords='django-rlog',
    description='Save rlog\'s Pub/Sub Log to Disk',
    long_description=open('README.rst').read(),

    url='https://github.com/django-xxx/django-rlog',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_rlog'],
    py_modules=[],
    install_requires=['django-six'],
    include_package_data=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
