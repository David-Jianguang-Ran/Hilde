from django.db                  import models
from django.contrib.auth.models import User
from hilde.utils                import debugPrintPlease

import uuid
# Create your models here.


class AccessUtilityMixin:
  """
  This class provides utility such as
  - uuid fields and generations
  - access control
  - serialization to json
  """
  # dran Can I assume no collision here?
  identifier          = models.UUIDField(null=False, default=uuid.uuid5, unique=True, primary_key=True)
  
  # dran I guess no need to define related name since we don't even know what the model is
  authorized_users    = models.ManyToManyField(User)
  
  # this field controls whether a model can be accessed via DatabaseView.get()
  exposed             = models.BooleanField(default=True)
  
  
  def serialize(self, depth=None):
    # TODO add complex thunking logic here
    return str(self)
  
  
class WebsocketTicket (AccessUtilityMixin, models):
  """
  attr:
  hash_key
  authorized_users
  """
  expired           = models.BooleanField(default=False)
  
  
  