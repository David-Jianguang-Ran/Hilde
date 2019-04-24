from django.shortcuts import render
from channels_websocket_utils.utils import get_websocket_token

# Create your views here.


def testy_view(request):
  token_str         = get_websocket_token(request.session)
  
  return render(request,"testy/testicle.html",context={"token":token_str})