from django.urls import path
from .views import static_view, live_view

urlpatterns = [
    path('title/',static_view,name='title'),
    path('title/main/',live_view,name='main')
]
