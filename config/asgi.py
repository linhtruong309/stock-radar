"""ASGI entry point. HTTP goes to Django; WebSocket routes are added in a later step."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter  # noqa: E402  (needs Django set up first)

application = ProtocolTypeRouter({"http": django_asgi_app})
