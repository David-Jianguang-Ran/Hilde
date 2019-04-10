import project.settings as settings

from .models import WebsocketTicket

import django.contrib.auth.models as authmod
import django.middleware.csrf


def debugPrintPlease(some_str):
  if settings.DEBUG:
    print("Debug Printout Below\n",some_str)


def getWebsocketKey(user):
  """
  This method generates a ws ticket and assigns the current user to it
  :param user: django User Obj
  :return: ticket.identifier uuid
  """
  new_ticket        = WebsocketTicket()
  new_ticket.authorized_users.add(user)
  new_ticket.save()
  return new_ticket.identifier


def validateWebsocketKey(user,ticket_identifier):
  # do we have a ticket?
  try:
    ticket          = WebsocketTicket.objects.get(identifier=ticket_identifier)
  except WebsocketTicket.DoesNotExist:
    debugPrintPlease("ws ticket validation failed for user {}".format(user))
    return False
  
  # is the ticket assigned to our user?
  try:
    user_match      = ticket.authorized_users.filter(username=user.username)
  except WebsocketTicket.DoesNotExist:
    debugPrintPlease("ws ticket validation failed for user {}".format(user))
    return False
  
  return True


def accessControl(required_perms):
  """
  This method is meant to enforce perms for a consumer method
  dran : Hey if you want to do custom perm you'll have to add it somewhere <= where? in the app
  also what happens when you check for a perm that doesn't exist?
  :param required_perms: list or tuple
  :return:
  """
  def _decorator(decoratee):
    # note that consumer method args look something like this:
    # args = (consumer_instance,event)
    
    def _failHandler(*args,**kwargs):
      debugPrintPlease("Method Access Denied for user: {} method: {}".format(args[0].scope['user'],decoratee))
    
    def _inner(*args,**kwargs):
      user = args[0].scope['user']
      
      if not user:
        return _failHandler(*args,**kwargs)
      
      if not user.has_perms(required_perms):
        return _failHandler(*args,**kwargs)
      else:
        return decoratee(*args,**kwargs)
      
    return _inner
  return _decorator



      

      
    
  
    
  