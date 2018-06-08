from django.conf.urls import url, include

from django.views.generic import RedirectView

from .views import UserDetailView, UserRegisterView


urlpatterns = [
	url(r'^', include("django.contrib.auth.urls")),
	url(r'^profile/(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='user_detail'),
	url(r'^register/$', UserRegisterView.as_view(), name='register'),

]