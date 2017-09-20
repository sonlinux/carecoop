"""
Django settings for Carecoop project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from django.core.urlresolvers import reverse_lazy
from os.path import dirname, join, exists

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__)))
MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()
import dj_database_url
# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authtools',
    'crispy_forms',
    'easy_thumbnails',

    'profiles',
    'accounts',
    # customly built APPS
    'members',
    'loanforms',
    'multimedia',
    'faq',
    'resources',
    'announcements',
    'home',
    'aboutus',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Carecoop.urls'

WSGI_APPLICATION = 'Carecoop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    'default': env.db(),
}


# Change 'default' database configuration with $DATABASE_URL.
#DATABASES['default'] = dj_database_url.config(conn_max_age=500)

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = join(BASE_DIR, 'static')
STATICFILES_DIRS = [join(BASE_DIR, 'static')]

ALLOWED_HOSTS = []

# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")

THUMBNAIL_EXTENSION = 'png'     # Or any extn for your thumbnails

SUIT_CONFIG = {
    # 'ADMIN_NAME': 'Admin app name',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': False,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': False, # Default True

    # menu
    # 'SEARCH_URL': 'admin:examples_country_changelist',
    # 'MENU':(
    #     # Rename app and set icon
    #     {'app': 'examples', 'icon':'icon-leaf', 'models': (
    #         'country', 'continent', 'kitchensink'
    #     )},
    #     {'label': 'Integrations', 'icon':'icon-globe', 'models': (
    #         'examples.city', 'examples.category', 'examples.wysiwygeditor',
    #         'examples.reversioneditem', 'examples.importexportitem'
    #     )},
    #
    #     {'app': 'cms', 'label': 'Django CMS', 'icon': 'icon-file', 'models': (
    #         'cms.page',
    #         'snippet.snippet',
    #         'cmsplugin_filer_image.thumbnailoption',
    #         'sites.site',
    #     )},
    #
    #     {'app': 'filer', 'label': 'Filer', 'icon': 'icon-picture',
    #      'url': '/admin/filer/', 'models': (
    #         {'model': 'filer.folder', 'label': 'Browse files'},
    #         {'model': 'filer.folderpermission', 'label': 'Permissions'},
    #     )},
    #     # '-',
    #     {'app': 'auth', 'models': ('user',), 'icon': 'icon-lock'},
    #
    #     {'label': 'Custom view', 'icon':'icon-cog', 'models': (
    #         {'label': 'Custom link', 'url': '/admin/custom/'},
    #         {'label': 'Check out error 404', 'url': '/admin/non-existant/'},
    #     )},
    # ),

    # misc
    'LIST_PER_PAGE': 15
}

AUTO_RENDER_SELECT2_STATICS = False

FILER_ENABLE_PERMISSIONS = True
THUMBNAIL_QUALITY = 100
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


# CMS
CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    # ('template_2.html', 'Template Two'),
)

gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
    ('ru', gettext('Russian')),
)

CMS_SHOW_START_DATE = True
CMS_SEO_FIELDS = True

SUIT_CONFIG = {
    'ADMIN_NAME': 'CARECOOP'
}
