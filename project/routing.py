from channels.auth    import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls      import path

from testy.consumers import TestyConsumer

application = ProtocolTypeRouter({
  # http views are already added by default
  
  "websocket" : AuthMiddlewareStack(
    URLRouter([
      path("ws/testy",TestyConsumer) # yuck!
    ])
    # add ws consumers here
  )
})