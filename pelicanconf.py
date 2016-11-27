#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ilya V. Schurov'
SITENAME = u'Math, Pics and Code'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = u'ru'
HTML_LANG = DEFAULT_LANG

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = "https://github.com/ischurov"

# Blogroll
LINKS = tuple()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/ivoyager'),
          ('facebook', 'https://facebook.com/ilyaschurov'),
          ('github', 'https://github.com/ischurov'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
THEME = "/Users/user/soft/pelican-sober-iv"
# THEME = "/Users/user/soft/pelican-themes/pelican-sober"
# RELATIVE_URLS = True
#
PELICAN_SOBER_ABOUT = """Меня зовут Илья Щуров. Математик. Любитель Py&shy;thon.
Пишу научные статьи со смешными названиями. Работаю в НИУ ВШЭ. Понемногу
программирую, фотографирую и путешествую."""

PELICAN_SOBER_TWITTER_CARD_CREATOR = "ivoyager"

