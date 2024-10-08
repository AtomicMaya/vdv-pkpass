"""
Django settings for vdv_pkpass project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import cryptography.x509
import cryptography.hazmat.primitives.serialization
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "")

DEBUG = False

ALLOWED_HOSTS = os.getenv("HOST", "vdv-pkpass.magicalcodewit.ch").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "govuk_frontend_django",
    "crispy_forms",
    "crispy_forms_gds",
    "main"
]

MIDDLEWARE = [
    "xff.middleware.XForwardedForMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "vdv_pkpass.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "vdv_pkpass.wsgi.application"

DATABASES = {
    'default': {
        "ENGINE": "django_cockroachdb",
        "HOST": os.getenv("DB_HOST", "localhost"),
        "NAME": os.getenv("DB_NAME", "vdv-pkpass"),
        "USER": os.getenv("DB_USER", "vdv-pkpass"),
        "PASSWORD": os.getenv("DB_PASS"),
        "PORT": '26257',
        "OPTIONS": {
            "application_name": os.getenv("APP_NAME", "vdv-pkpass"),
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [{
    "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
}, {
    "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
}, {
    "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
}, {
    "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
}]

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

EXTERNAL_URL_BASE = os.getenv("EXTERNAL_URL", f"https://{ALLOWED_HOSTS[0]}")

STATIC_URL = os.getenv("STATIC_URL", f"{EXTERNAL_URL_BASE}/static/")
MEDIA_URL = os.getenv("MEDIA_URL", f"{EXTERNAL_URL_BASE}/media/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_ALLOWED_TEMPLATE_PACKS = ["gds"]
CRISPY_TEMPLATE_PACK = "gds"

XFF_TRUSTED_PROXY_DEPTH = 1
XFF_NO_SPOOFING = True
XFF_HEADER_REQUIRED = True

AWS_S3_CUSTOM_DOMAIN = os.getenv("S3_CUSTOM_DOMAIN", "")
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_S3_REGION_NAME = os.getenv("S3_REGION", "")
AWS_S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT", "")
AWS_STORAGE_BUCKET_NAME = os.getenv("S3_BUCKET", "")
AWS_S3_ACCESS_KEY_ID = os.getenv("S3_ACCESS_KEY_ID", "")
AWS_S3_SECRET_ACCESS_KEY = os.getenv("S3_SECRET_ACCESS_KEY", "")
AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_S3_SIGNATURE_VERSION = "s3v4"

STORAGES = {
    "default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
    "staticfiles": {"BACKEND": "storages.backends.s3boto3.S3ManifestStaticStorage"},
    "vdv-certs": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "bucket_name": "vdv-certs",
        }
    },
    "uic-data": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "bucket_name": "uic-data",
        }
    },
}

with open(os.getenv("WWDR_CERTIFICATE_LOCATION"), "rb") as f:
    WWDR_CERTIFICATE = cryptography.x509.load_der_x509_certificate(f.read())
with open(os.getenv("PKPASS_CERTIFICATE_LOCATION"), "rb") as f:
    PKPASS_CERTIFICATE = cryptography.x509.load_der_x509_certificate(f.read())
with open(os.getenv("PKPASS_KEY_LOCATION"), "rb") as f:
    PKPASS_KEY = cryptography.hazmat.primitives.serialization.load_pem_private_key(f.read(), None)

PKPASS_CONF = {
    "organization_name": os.getenv("PKPASS_ORGANIZATION_NAME"),
    "pass_type": os.getenv("PKPASS_PASS_TYPE"),
    "team_id": os.getenv("PKPASS_TEAM_ID"),
}

AZTEC_JAR_PATH = BASE_DIR / "aztec-1.0.jar"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'console_debug_false': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_debug_false'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}