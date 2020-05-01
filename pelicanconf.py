#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'MxCog'
SITENAME = 'Example'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# THEME = 'bootstrap-next'
THEME = 'pelican-bootstrap3'

# Bootstrap theme settings
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']
# Set this to change bootswatch (http://bootswatch.com/)
BOOTSTRAP_THEME = 'superhero'

# Blogroll
LINKS = (('Admin', 'admin'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/company/blockdox/'),
          ('Twitter', 'https://twitter.com/blockdoxuk'),)

DEFAULT_PAGINATION = False

STATIC_PATHS = [
    'admin/index.html',
    'admin/config.yml',
    'images',
    'extra'
]

PAGE_EXCLUDES = [
    'admin'
]

ARTICLE_EXCLUDES = [
    'admin'
]

EXTRA_PATH_METADATA = {
    # 'extra/custom.css': {'path': 'custom.css'},
    # 'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    # 'extra/CNAME': {'path': 'CNAME'},
    # 'extra/LICENSE': {'path': 'LICENSE'},
    # 'extra/README': {'path': 'README'},
}

# Import local development config
try:
    import pelicanconf_local
except ImportError:
    pass
