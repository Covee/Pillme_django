from django.conf.urls import url, include

from django.views.generic import RedirectView

from .views import UserDetailView


urlpatterns = [
	# url(r'^', include("django.contrib.auth.urls")),
	url(r'^(?P<pk>[\w.@+-]+)/$', UserDetailView.as_view(), name='user_profile'),
	# url(r'^register/$', UserRegisterView.as_view(), name='register'),
	
	
]