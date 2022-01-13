import os
from datetime import timedelta
from gettext import gettext

import dj_database_url

"""
Django settings for config project.
Generated by 'django-admin startproject' using Django 3.1.12.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "")
PACKAGE_DIR = os.path.join(ROOT_DIR, "kft_core")


def public_assets():
    return os.path.join(ROOT_DIR, os.path.pardir, "public_assets")


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = os.getenv("DJANGO_DEBUG", True) == "TRUE"
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY", "3@^u#g9nw236c_#d-6dah(qupxmt(2s2s-&i(1%yemlbe057i+"
)
ALLOWED_HOSTS = [
    "*",
]
SILENCED_SYSTEM_CHECKS = []
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Asia/Kuwait"

# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-US"
LANGUAGES = (("ar", gettext("Arabic")), ("en", gettext("English")))
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [os.path.join(ROOT_DIR, "locale")]

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# Append_slash to urls https://docs.djangoproject.com/en/3.0/ref/settings/#append-slash
APPEND_SLASH = False
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"
# APPS
# ------------------------------------------------------------------------------

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "rest_framework_swagger",
    "django_extensions",
]

LOCAL_APPS = [
    "ob_dj_survey.core.survey",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Django-Templates
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# DATABASES
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://postgres:password@db:5432/db")
DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}
# "default": dj_database_url.parse(DATABASE_URL),
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = os.getenv("STATIC_URL", "/static/")
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [os.path.join(ROOT_DIR, "static")]

# Static Root
STATIC_ROOT = public_assets()

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
# MEDIA_URL from OS env or append `ROOT_DIR/media` for default
MEDIA_ROOT = os.getenv("MEDIA_ROOT", os.path.join(ROOT_DIR, "media"))
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = os.getenv("MEDIA_URL", "/media/")

# Maximum size, in bytes, of a request before it will be streamed to the
# file system instead of into memory.
FILE_UPLOAD_MAX_MEMORY_SIZE = int(
    os.getenv("FILE_UPLOAD_MAX_MEMORY_SIZE", 2621440)
)  # i.e. 2.5 MB

# Maximum size in bytes of request data (excluding file uploads) that will be
# read before a SuspiciousOperation (RequestDataTooBig) is raised.
DATA_UPLOAD_MAX_MEMORY_SIZE = int(
    os.getenv("DATA_UPLOAD_MAX_MEMORY_SIZE", 2621440)
)  # i.e. 2.5 MB

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
# FIXTURE_DIRS = (str(APPS_DIR.path("fixtures")),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 3600 * 24 * 1  # 1 day
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# ADMIN
ADMIN_ENABLED = False
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = []
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND", "django.core.mail.backends.locmem.EmailBackend"
)
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-timeout
EMAIL_FROM = os.environ.get("EMAIL_FROM")
AWS_SES_REGION_NAME = os.getenv("AWS_DEFAULT_REGION")
AWS_SES_REGION_ENDPOINT = os.getenv("AWS_SES_REGION_ENDPOINT")
# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "root": {"level": "WARNING", "handlers": ["console"]},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "loggers": {
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        "raven": {"level": "DEBUG", "handlers": ["console"], "propagate": False},
    },
}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# DRF/JWT
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50,
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "TEST_REQUEST_RENDERER_CLASSES": [
        "rest_framework.renderers.MultiPartRenderer",
        "rest_framework.renderers.JSONRenderer",
    ],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
}


# Django Survey
# ------------------------------------------------------------------------------
# Add settings later