#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'BlockDox'
SITENAME = 'BlockDox'
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

# Menu
MENUITEMS = [
    ('About', '/category/about.html'),
    ('Smart Buildings', '/category/smart-buildings.html'),
    ('Passenger Count', '/category/passenger-count.html'),
    ('Social Distancing', '/category/social-distancing.html'),
    ('News & Articles', '/category/news-articles.html'),
    ('Contact', '/pages/contact.html')
]

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# THEME = 'bootstrap-next'
THEME = 'blockdox-bootstrap3'

# Bootstrap theme settings
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'image_process', 'image_category_class']
# Set this to change bootswatch (http://bootswatch.com/)
BOOTSTRAP_THEME = 'flatly'
CUSTOM_CSS = 'static/css/custom.css'

SITELOGO = 'images/logo-white.png'
SITELOGO_SIZE = 100
HIDE_SITENAME = True

SHOW_ARTICLE_CATEGORY = True

IMAGE_PROCESS = {
    'article-summary-image': ["scale_in 200 200 True"],
    'article-image': ["scale_in 500 500 True"],
    'page-image': ["scale_in 500 500 True"]
}
IMAGE_PROCESS_DIR = 'processed'
# For development always process
# IMAGE_PROCESS_FORCE = True

# Blogroll
LINKS = (
    ('BlockDox.com', 'http://blockdox.com'),
)

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
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/Forza-Medium.otf': {'path': 'static/fonts/Forza-Medium.otf'},
    # 'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    # 'extra/CNAME': {'path': 'CNAME'},
    # 'extra/LICENSE': {'path': 'LICENSE'},
    # 'extra/README': {'path': 'README'},
}

DISPLAY_ARTICLE_INFO_ON_INDEX = True

NETLIFY_CMS = True

# Import local development config
try:
    import pelicanconf_local
except ImportError:
    pass
