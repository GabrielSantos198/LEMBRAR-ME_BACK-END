"""
ASGI config for LEMBRAR_ME_BACK_END project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LEMBRAR_ME_BACK_END.settings')

application = get_asgi_application()
