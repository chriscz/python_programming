#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# During Plugin debugging
LOAD_CONTENT_CACHE = False

# --- define plugins
#PLUGINS =  ['disqus_python']


AUTHOR = u'Mike & Chris'
SITENAME = u'Programming in Python'

#SITEURL=''
SITEURL = 'https://chriscz.github.io/python_programming'



PATH = 'content'

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = []
#(('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = []
#(('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


THEME = 'notmyidea-cms' 
DISQUS_SITENAME="pythonprogramming"

# --- Theme specific configuration
#THEME = 'pelican-mg' 
#TAG_SAVE_AS = ''
#AUTHOR_SAVE_AS = ''
#DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
#TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'


STATIC_PATHS = ['resources']
