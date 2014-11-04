from django.conf.urls import patterns, include, url
#from views import home

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns(
	'',
	#url(r'^$', TemplateView.as_view(template_name='home.html')),

	url(r'^$', 				'books.views.bholder'),
	url(r'thebigjob',  	'books.views.thebigjob'),
	url(r'booboobear', 	'books.views.booboobear'),
	url(r'tbd', 			'books.views.tbd'),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)),)
#    urlpatterns += staticfiles_urlpatterns()
