from movie_pro.settings import *
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.sitemaps',

    'bootstrap_modal_forms',
    'widget_tweaks',
    'debug_toolbar',
    'star_ratings',
    'taggit',
    'robots',
    'ckeditor',
    'captcha',
    'compressor',

    'website.apps.WebsiteConfig',
    'movie.apps.MovieConfig',
    'blog.apps.BlogConfig',
    'account.apps.AccountConfig'
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Site id

SITE_ID = 3


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []


# Django Debug Toolbar Configuration

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('NAME'),
        'HOST': os.getenv('HOST'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
    }
}
