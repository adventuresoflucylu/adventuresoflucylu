"""Common settings and globals."""


from os.path import abspath, basename, dirname, join, normpath
from sys import path
import os

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Admin', 'admin@adventuresoflucylu.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.',
#        'NAME': '',
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '',
#    }
    'lucyludb': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/Los_Angeles'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
#SITE_ID = 2

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION

########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
#MEDIA_ROOT = os.path.join(SITE_ROOT,'/media')
MEDIA_ROOT = '/usr/local/adventuresoflucylu.com/media'
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION

########## ADMIN MEDIA CONFIGURATION
ADMIN_MEDIA_PREFIX = '/static/admin/'
########## END ADMIN MEDIA CONFIGURATION

########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
#STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
#SECRET_KEY = r"%4@2c)7^*ctgu&7*u5seqsl@8h62x4ttdivp^m^6m+ox@qmoeu"
SECRET_KEY = "%4@2c)7^*ctgu&7*u5seqsl@8h62x4ttdivp^m^6m+ox@qmoeu"
########## END SECRET CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
########## END SITE CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
#	Required by allauth template tags
	'django.core.context_processors.request',
	'django.contrib.auth.context_processors.auth',
#	allauth specific context processors
	'allauth.account.context_processors.account',
	'allauth.socialaccount.context_processors.socialaccount',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
#    'django.template.loaders.filesystem.Loader',
#	'django.template.loaders.app_directories.Loader',
#	'django.template.loaders.app_directories.Loader',
#	'django.template.loaders.filesystem.Loader',
TEMPLATE_LOADERS = (
	'django.template.loaders.app_directories.Loader',
	'django.template.loaders.filesystem.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
#    normpath(join(SITE_ROOT, 'home/templates')),
#    normpath(join(SITE_ROOT, 'books/templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
	# Default Django middleware.
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION

########## AUTHENTICATION PROFILE CONFIGURATION
## Below is an example of configure the env varible
## AUTH_PROFILE_MODULE = 'app.UserProfile' 
## (note app.Model, not models.UserProfile) where app is the name of your app

# provide our get_profile()
#AUTH_PROFILE_MODULE = 'users.BookUser'
########## END AUTHENTICATION PROFILE CONFIGURATION

########## AUTHENTICATION BACKENDS CONFIGURATION
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
########## END AUTHENTICATION BACKENDS CONFIGURATION

########## APP CONFIGURATION
DJANGO_APPS = (
	# Default Django apps:
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.flatpages',

	# Useful template tags:
	# 'django.contrib.humanize',

	# Admin panel and documentation:
	'django.contrib.admin',
	# 'django.contrib.admindocs',
)

# Apps specific for this project go here.
LOCAL_APPS = (

	# User account authorization:
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
# 	... include the providers you want to enable:
#	'allauth.socialaccount.providers.twitch',
#	'allauth.socialaccount.providers.facebook',
#	'allauth.socialaccount.providers.flickr',
#	'allauth.socialaccount.providers.google',
#	'allauth.socialaccount.providers.instagram',
#	'allauth.socialaccount.providers.twitter',
	'home',
	'books',
	'bassethounds',
	'aboutus',
	'users',
	'tinymce',
	'flatpages_tinymce',
	'bootstrapform',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
########## END APP CONFIGURATION

########## REGISTRATION CONFIGURATION
# URL for @login_required decorator to use
LOGIN_URL = '/login/'
# redirect authenticated users
LOGIN_REDIRECT_URL = '/profile/'
#LOGIN_REDIRECT_URL = '/books/booboobear/'

SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
#    'facebook': {
#        'SCOPE': ['email', 'publish_stream'],
#        'METHOD': 'js_sdk'  # instead of 'oauth2'
#    }
}

#ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
EMAIL_USE_TLS = True
EMAIL_HOST ='localhost'
#EMAIL_HOST ='smtp.1and1.com'
#EMAIL_HOST_USER = 'admin@adventutesoflucylu.com'
#EMAIL_HOST_PASSWORD = 'oV@eN#E<Quart#'
##SERVER_EMAIL = 'admin@adventutesoflucylu.com'
#DEFAULT_FROM_EMAIL = 'Adventures of Lucy Lu Books'
########## END REGISTRATION CONFIGURATION

########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
########## END WSGI CONFIGURATION


########## SOUTH CONFIGURATION
# See: http://south.readthedocs.org/en/latest/installation.html#configuring-your-django-installation
INSTALLED_APPS += (
    # Database migration helpers:
#    'south',
)
# Don't need to use South when setting up a test database.
SOUTH_TESTS_MIGRATE = False
########## END SOUTH CONFIGURATION


########## NEW RELIC CONFIGURATION 
#NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program command options
########## NEW RELIC CONFIGURATION
