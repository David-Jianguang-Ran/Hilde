from channels.auth    import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
# from hilde.consumers  import Dispatcher


application = ProtocolTypeRouter({
  # http views are already added by default
  
  "websocket" : AuthMiddlewareStack(
    URLRouter([
    
    ])
    # add ws consumers here
  )
  
  # "channel"   : ChannelNameRouter({
  #   # some name - consumer pairs
  #   "Dispatcher" : Dispatcher
  # })
})