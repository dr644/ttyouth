import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = True
ALLOWED_HOSTS = ['www.ttyouth.org']
STATIC_ROOT = []
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]