"""
Django settings for boss project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import logging
import django.utils.log
import logging.handlers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IN_DIR = os.path.join(BASE_DIR, 'bsconf', 'data', 'in')
TPL_DIR = os.path.join(BASE_DIR, 'bsconf', 'data', 'template')
OUT_DIR = os.path.join(BASE_DIR, 'bsconf', 'data', 'out')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x2i!5ga!m#+=yl4)wgt_jg!f-9w5uaf-0-fs%46(#6_5@-+xe-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['10.4.144.245','10.4.8.79']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bsconf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'boss.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'boss.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'ng1tst01',
        'USER': 'zg',
        'PASSWORD': 'ngboss4,123',
        'HOST': '10.7.5.132',
        'PORT': '1521',
    },
    'base': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'ng1tst01',
        'USER': 'base',
        'PASSWORD': 'base',
        'HOST': '10.7.5.132',
        'PORT': '1521',
    },
    'test2': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'ngtst02',
        'USER': 'zg',
        'PASSWORD': 'ngboss4,123',
        'HOST': '10.7.5.164',
        'PORT': '1521',
    },
    'prod': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'scdb',
        'USER': 'ad',
        'PASSWORD': 'ad',
        'HOST': '10.4.84.17',
        'PORT': '1521',
    }
}

# use multi-database in django
# add by wxt
DATABASE_ROUTERS = ['boss.database_router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {
    # example:
    #'app_name':'database_name',
    'base': 'base',
    'test2': 'test2',
    'prod': 'prod',
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'datefmt': '%Y%m%d%H%M%S',
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(process)d:%(thread)d] [%(levelname)s]- %(message)s'},  #标准日志格式  %(ip)s-%(username)s
        'exceptfmt': {
            'format': '%(asctime)s [%(process)d:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'},  #异常日志格式 %(ip)s-%(username)s
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/dictation.log'),     #日志输出文件
            'when': 'midnight',                  #文件大小
            'interval': 1,
            'backupCount': 5,                         #备份份数
            # 'datefmt': '%Y%m%d%H%M%S',
            'formatter':'standard',                   #使用哪种formatters日志格式
            # 'suffix': "%Y-%m-%d_%H-%M-%S.log",
        },
        'error': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/dictation.err'),
            'maxBytes':1024*1024*5,
            'backupCount': 5,
            'formatter':'exceptfmt',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/script.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
        },
        'scripts_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':os.path.join(BASE_DIR, 'log/script.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'error': {
            'handlers': ['error', 'console'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'scripts': {
            'handlers': ['scripts_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'sourceDns.webdns.views': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': True
        },
        'sourceDns.webdns.util':{
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}
