from pathlib import Path
import os


#from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load our environmental variables
# load_dotenv()



# # password DB
# DB_PASSWORD_YO = os.environ['DB_PASSWORD_YO']


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x4m$gfeda-r+)u05g*bzm%8#_vz&8-wl^3epo45gqi#_eqwvtq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app']
CSRF_TRUSTED_ORIGINS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'cart',
    'payment',
    'whitenoise.runserver_nostatic',
    'paypal.standard.ipn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'ecom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',

            ],
        },
    },
]

WSGI_APPLICATION = 'ecom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',                  # Your database name
        'USER': 'postgres.jxegrzviztasnwbzxzqa',                     # Your username
        'PASSWORD': 'frizel1256,',     # Your password
        'HOST': 'aws-0-eu-central-1.pooler.supabase.com',               # Your host
        'PORT': '5432',                         # Your port
    }
}




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = ['static/']

# White noise static stuff
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'

SUPABASE_URL='https://jxegrzviztasnwbzxzqa.supabase.co'
SUPABASE_API_KEY='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp4ZWdyenZpenRhc253Ynp4enFhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMDQxOTYzNCwiZXhwIjoyMDQ1OTk1NjM0fQ.78xvfqGIincye-31VOZ3fzOvjTvy4N7lpI_xWORugNA'

# settings.py

# Use Supabase as the default file storage backend
DEFAULT_FILE_STORAGE = 'store.storage.SupabaseStorage'

# Supabase credentials
SUPABASE_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp4ZWdyenZpenRhc253Ynp4enFhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMDQxOTYzNCwiZXhwIjoyMDQ1OTk1NjM0fQ.78xvfqGIincye-31VOZ3fzOvjTvy4N7lpI_xWORugNA'  # Replace with your actual API key
SUPABASE_URL = 'https://jxegrzviztasnwbzxzqa.supabase.co'  # Replace with your Supabase project URL
SUPABASE_ROOT_PATH = 'product-images/'  # Root path for media files; customize as needed

# Define MEDIA_URL for referencing files in templates or views
MEDIA_URL = f'{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_ROOT_PATH}'



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Add paypal settings
# Set sandbox to true
PAYPAL_TEST = True

PAYPAL_RECEIVER_EMAIL = '' # Business Sandbox account
