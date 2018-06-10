from django.shortcuts import render
from django.conf.urls import url, include

from .views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
	# url(r'^pill_detail/(?P<pk>\d+)/$', PillDetailView.as_view(), name='pill_detail'),

]