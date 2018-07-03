from django.urls import path
from .views import static_view,react_enabled_view,js_enabled_view

urlpatterns = [
    path('', static_view, name='static'),
    path('js/', js_enabled_view, name='js'),
    path('react/',react_enabled_view,name='react')
]
