"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

sys.path.append('/app/website/settings')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
