#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Илья Щуров'
SITENAME = u'Math, Pics and Code: блог Ильи Щурова'
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
LINKS = (('страница на сайте НИУ ВШЭ', 'http://hse.ru/staff/is'),
        ('статьи на arXiv', 'https://arxiv.org/a/schurov_i_1.html'),
        )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/ivoyager'),
          ('facebook', 'https://facebook.com/ilyaschurov'),
          ('github', 'https://github.com/ischurov'),
          ('stackoverflow',
          'http://stackoverflow.com/users/3025981/ilya-v-schurov'),
          ('flickr', 'http://flickr.com/photos/ivoyager')
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
THEME = "/Users/user/soft/pelican-sober-iv"
# THEME = "/Users/user/soft/pelican-themes/elegant"
# RELATIVE_URLS = True
#
PELICAN_SOBER_ABOUT = """Меня зовут Илья Щуров. Ма&shy;те&shy;ма&shy;тик. Лю&shy;би&shy;тель пи&shy;тон&shy;чи&shy;ков.
Пишу на&shy;учные статьи со смешными названиями. Работаю в НИУ ВШЭ. Преподаю. Понемногу
про&shy;грам&shy;ми&shy;рую, фото&shy;гра&shy;фи&shy;рую и пу&shy;те&shy;шес&shy;твую."""

PELICAN_SOBER_TWITTER_CARD_CREATOR = "ivoyager"
PELICAN_SOBER_STICKY_SIDEBAR = False
IGNORE_FILES = ['.ipynb_checkpoints']
PELICAN_SOBER_IV_FACEBOOK_APP_ID = '454295064733340'
