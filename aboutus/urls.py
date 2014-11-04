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
	url(r'lucylu-about',	'bassethounds.views.holder'),
	url(r'maxwell-about',	'bassethounds.views.holder'),
	url(r'mommyndaddy-about',	'bassethounds.views.holder'),
#	url(r'^$',	'bassethounds.views.bholder'),
#	url(r'me',	'bassethounds.views.me'),
#	url(r'booboobear',	'bassethounds.views.booboobear'),
#	url(r'mommyndaddy',	'bassethounds.views.mommyndaddy'),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)),)
#    urlpatterns += staticfiles_urlpatterns()
