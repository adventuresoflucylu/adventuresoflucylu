# main url

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from home import views

urlpatterns = [
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    url(r'^contact/$', 'home.views.contact', name='contact'),
    # url(r'^about/$', 'advllproject.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^books/', include('books.urls')),
    url(r'^aboutus/', include('aboutus.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)