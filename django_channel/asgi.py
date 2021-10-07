"""
ASGI config for django_channel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.routing import  URLRouter
import Channel.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channel.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            Channel.routing.websocket_urlpatterns
        )
    ),
})