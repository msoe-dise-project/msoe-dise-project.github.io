AUTHOR = 'RJ Nowling'
SITENAME = 'MSOE DISE Project'
SITEURL = 'https://msoe-dise-project.github.io'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

INDEX_SAVE_AS = 'all_articles.html'

# Blogroll
LINKS = (('RJ Nowling', 'https://rnowling.github.io'),
         ('MSOE', 'https://www.msoe.edu'),)

# Social widget
SOCIAL = tuple()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Home', '/'),
    ('Course Materials', '/pages/course-materials.html'),
    ('Articles', '/pages/articles.html'),
    ('GitHub', 'https://github.com/msoe-dise-project'),
    ('Project Members', '/pages/project_members.html'),
    )
