from django.contrib.sessions.models import Session
from django.db                      import models
import uuid


# Create your models here.
class WebsocketToken (models.Model):
  """
  
  """
  token             = models.UUIDField(null=False, default=uuid.uuid4, unique=True, primary_key=True)
  
  session           = models.ForeignKey(Session, on_delete=models.SET_NULL)
  
  expired           = models.BooleanField(default=False)