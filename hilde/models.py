from django.db                    import models
from django.contrib.auth.models   import AbstractUser
from django.conf                  import settings
from django.core.serializers      import serialize
from hilde.utils                  import debugPrintPlease

import uuid



class User (AbstractUser):
  # Pass for now, but laying groundwork for custom user class in the future
  pass


class AccessUtilityMixin:
  """
  This class provides utility such as:
  - uuid fields and generations
  - access control
  - serialization to json
  """
  # dran Can I assume no collision here?
  identifier          = models.UUIDField(null=False, default=uuid.uuid4, unique=True, primary_key=True)
  
  # dran I guess no need to define related name since we don't even know what the model is
  authorized_users    = models.ManyToManyField(settings.AUTH_USER_MODEL,null=True,on_delete=SET_NULL)
  
  # this field controls whether a model can be accessed via DatabaseView.get()
  exposed             = models.BooleanField(default=True)
  
  
  def serialize(self, depth=None):
    # TODO add complex thunking logic here
    return serialize("json",self)
  
  
class WebsocketTicket (AccessUtilityMixin, models):
  """
  attr:
  hash_key
  authorized_users
  """
  expired           = models.BooleanField(default=False)
  
  
  