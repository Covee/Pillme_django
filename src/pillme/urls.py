from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

from .views import home_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name='home'),
    url(r'^pills/', include("pills.urls", namespace="pills")),
    
    url(r'^accounts/', include('allauth.urls')),  # for allauth

    url(r'^profiles/', include('accounts.urls', namespace='profiles')),


	# url(r'^accounts/', include('accounts.urls', namespace='accounts')),
	url(r'^freeboard/', include('posts.urls', namespace='freeboard')),


] 

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
