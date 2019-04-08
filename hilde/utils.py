import project.settings as settings

from .models import WebsocketTicket

import django.contrib.auth.models as authmod

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


def accessControl(some_method,user=None,required_perm=None):
  """
  TODO figure out how does decorators work with arguments
  Hey if you want to do custom perm you'll have to add it somewhere in the app
  :param some_method:
  :param user:
  :param required_perm:
  :return:
  """
  user = authmod.User
  if user.has_perm(required_perm):
    some_method()
    
  