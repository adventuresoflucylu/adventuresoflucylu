# Aboutus urls

# from django.conf.urls import patterns, include, url
# from . import views
#
# urlpatterns = [
#   url(r'',            views.aboutus,      name='aboutus'),
#   url(r'lucylu/',     views.lucylu,       name='lucylu'),
#   url(r'mytime',      views.mytime,       name='mytime'),
#   url(r'maxwell',     views.maxwell,      name='maxwell'),
#   url(r'mommyndaddy',  views.mommyndaddy,  name='mommyndaddy'),
# ]

from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = [
  url(r'^$',            views.aboutus,      name='aboutus'),
  url(r'lucylu',        views.lucylu,       name='lucylu'),
  url(r'mytime',        views.mytime,       name='mytime'),
  url(r'maxwell',       views.maxwell,      name='maxwell'),
  url(r'mommyndaddy',   views.mommyndaddy,  name='mommyndaddy'),
]
