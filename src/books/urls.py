# Books urls
from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = [
  url(r'^$',              views.books,        name='books'),
  url(r'thebigjob',       views.thebigjob,    name='thebigjob'),
  url(r'goingtoohio',     views.goingtoohio,  name='goingtoohio'),
  url(r'booboobear',      views.booboobear,   name='booboobear'),
  url(r'tbd',             views.tbd,          name='tbd'),
]
