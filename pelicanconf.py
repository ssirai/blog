#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = 'ssirai'
SITENAME = 'גולם壱佰'
# SITEURL = 'http://ssirai.github.io/blog'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None # 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None # 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Archive', 'archives.html'),)

path = os.path.join(os.environ.get('HOME'), 'dev/projects')
THEME = '%s/pelican-themes/pelipress' % path

REVERSE_ARCHIVE_ORDER = 1
DIRECT_TEMPLATES = ('index', 'categories', 'archives')

PLUGIN_PATH = '%s/pelican-plugins' % path
PLUGINS = ['liquid_tags.notebook', 'latex']
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

DEFAULT_PAGINATION = 10

DEFAUT_DATE_FORMAT = '%Y %B %d'

ARTICLE_URL     = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

