from django.conf.urls import url, include
from django.contrib import admin

from .views import home_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name='home'),
    
]
