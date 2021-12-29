AUTHOR = 'Rafa Luque'
SITENAME = 'Highnoon Ruffles'
SITEURL = 'https://highnoon-ruffles.com'
THEME = 'theme'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'


SITESUBTITLE = "One endless rabbit hole"
BIO = "One endless rabbit hole"
PROFILE_IMAGE = 'calling.jpg'
FOOTER_TEXT = '© 2021. Rafa Luque. All rights reserved.'
COLOR_THEME = '0x'
DIRECT_TEMPLATES = ['index', 'archives']
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
ARCHIVES_SAVE_AS = 'archive.html'

MENUITEMS = (
        ('Archive', 'archive.html'),
        )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (('twitter', 'https://twitter.com/rafa_luque'),
        ('github', 'https://github.com/rlooq'),
        ('email', 'rlooq@yahoo.com')
        )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
