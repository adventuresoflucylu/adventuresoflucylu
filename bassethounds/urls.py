from django.conf.urls import patterns, include, url
#from views import home

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns(
	'',
	#url(r'^$', TemplateView.as_view(template_name='home.html')),
#	url(r'^thebreed TemplateView.as_view(template_name='/templates/holder.html')),
#	url(r'^$', TemplateView.as_view(template_name='home.html')),

	url(r'^$',	'bassethounds.views.bholder'),
	url(r'thebreed',	'bassethounds.views.holder'),
	url(r'rescues',	'bassethounds.views.holder'),
#	url(r'thebread',	'bassethounds.views.thebreed'),
#	url(r'rescues',	'bassethounds.views.rescues'),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)),)
#    urlpatterns += staticfiles_urlpatterns()
