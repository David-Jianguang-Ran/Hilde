import project.settings as settings
from .models import WebsocketToken


def debug_print(some_str):
  if settings.DEBUG:
    print("Debug Printout Below\n",some_str)


def get_websocket_token(session):
  """
  
  :param session: django session obj
  :return:
  """
  new_token         = WebsocketToken()
  new_token.session = session
  new_token.save()
  return new_token.token_str


def validate_websocket_token(session, token_str):
  """
  
  :param session:
  :param token:
  :return:
  """
  # do we have a token?
  try:
    token = WebsocketToken.objects.get(token_str=token_str)
  except WebsocketToken.DoesNotExist:
    debug_print("ws ticket validation failed for session {}".format(session))
    return False
  # is the token assigned to current session?
  if session is token.session:
    return True
  else:
    return False
