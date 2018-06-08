from django.conf.urls import url, include

from django.views.generic import RedirectView

from .views import UserDetailView

urlpatterns = [
	url(r'^accounts/', include("django.contrib.auth.urls")),
	url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),

]