from django.shortcuts import render
from django.conf.urls import url, include

from .views import PostListView


urlpatterns = [
    # url(r'^$', HomeView.as_view(), name='home'),
    url(r'^$', PostListView.as_view(), name='post_list'),
	# url(r'^pill_detail/(?P<pk>\d+)/$', PillDetailView.as_view(), name='pill_detail'),

]