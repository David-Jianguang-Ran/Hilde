from .utils import debug_print


###
##
# Decorators for function based views
# TODO Add function based django view decorator for attaching websocket token to context

###
##
# Decorators for Consumer Methods
# TODO make async versions for these decorators
def require_perms(required_perms):
  """
  This decorator is meant to enforce perms for a consumer method
  dran : Hey if you want to do custom perm you'll have to add it somewhere <= where? in the app
  also what happens when you check for a perm that doesn't exist?
  :param required_perms: list or tuple
  :return:
  """
  def _decorator(decoratee):
    # note that consumer method args look something like this:
    # args = (consumer_instance,event)
    
    def _fail_handler(*args, **kwargs):
      debug_print("Method Access Denied for user: {} method: {}".format(args[0].scope['user'], decoratee))
    
    def _inner(*args, **kwargs):
      user = args[0].scope['user']
      
      if not user:
        return _fail_handler(*args, **kwargs)
      
      if not user.has_perms(required_perms):
        return _fail_handler(*args, **kwargs)
      else:
        return decoratee(*args, **kwargs)
    
    return _inner
  
  return _decorator


# TODO write JS ws manager method to work with this
def auto_route(decoratee):
  """
  This decorator is meant attach a reply key then send response down ws connection
  WHen used with ws manager, this method can automatically route message to the js component
  :param decoratee:
  :return:
  """
  # note that consumer method args look something like this:
  # args = (consumer_instance,event)
  def _inner(*args, **kwargs):
    reply_key = args[1]['reply_key']
    
    result = decoratee(*args, **kwargs)
    result['key'] = reply_key
    
    args[0].send_json(result)
  
  return _inner



