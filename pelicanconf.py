#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ssirai'
SITENAME = 'גולם壱佰'
SITEURL = 'http://ssirai.github.io/blog'

# TIMEZONE = 'Japan/Osaka'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None # 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None # 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Archive', 'archives.html'),)
REVERSE_ARCHIVE_ORDER = 1
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives')

# Social widget
# SOCIAL = (('github', 'https://github.com/ssirai'))

DEFAULT_PAGINATION = 10

DEFAUT_DATE_FORMAT = '%Y %B %d'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL     = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

