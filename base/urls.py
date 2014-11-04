from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView
#from views 	import home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#//	url(r'^$', TemplateView.as_view(template_name='home/home.html')),
urlpatterns = patterns('',
#	url(r'^$', TemplateView.as_view(template_name='home.html')),

    # Examples:
    # url(r'^$', 'lucylu.views.home', name='home'),
    # url(r'^lucylu/', include('lucylu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^tinymce/', include('books.urls')),
#	url(r'^accounts/', include('allauth.urls')),
	url(r'^$', include('home.urls')),
	url(r'^books/', include('books.urls')),
	url(r'^bassethounds/', include('bassethounds.urls')),
	url(r'^aboutus/', include('aboutus.urls')),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	import debug_toolbar
	urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)),)
#	urlpatterns += staticfiles_urlpatterns()
