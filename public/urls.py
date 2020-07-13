from django.conf.urls import url
from django.urls import path
from .views import home

urlpatterns = [
    path('', home.index, name='index'),
    path('switch_to_language_link/<language>', home.switch_to_language_link, name='switch_to_language_link'),
    path('apple-touch-icon.png', home.apple_touch_icon_png, name='apple_touch_icon_png'),
    path('favicon.png', home.favicon_png, name='favicon_png'),
    path('favicon.ico', home.favicon_ico, name='favicon_ico'),
]