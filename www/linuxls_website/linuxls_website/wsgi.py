"""
WSGI config for linuxls_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import os
import sys
from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.join(BASE_DIR, 'linuxls_website')

print(BASE_DIR)
print(PROJ_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linuxls_website.settings')

sys.path.append(BASE_DIR)
sys.path.append(PROJ_DIR)

application = get_wsgi_application()
