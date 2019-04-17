from channels.generic.websocket import JsonWebsocketConsumer
from channels_websocket_utils.utils import validate_websocket_token


class TestyConsumer(JsonWebsocketConsumer):
  def connect(self):
    token_str       = self.scope['kwargs']['token']
    
    # only accept connection if it provided a valid token in url kwargs
    if validate_websocket_token(self.scope['session'],token_str):
      self.accept()
    else:
      self.close()
      
  def echo_back(self,event):
    data            = event.data
    data['key']     = 'echo'
    self.send_json(data)