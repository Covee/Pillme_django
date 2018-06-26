from django.shortcuts import render
from django.conf.urls import url, include

from .views import PostCreateView, PostListView, PostDetailView, PostCountHitDetailView


urlpatterns = [
    # url(r'^$', HomeView.as_view(), name='home'),
	url(r'^create/$', PostCreateView.as_view(), name='post_create'),
    url(r'^$', PostListView.as_view(), name='post_list'),
	url(r'^(?P<pk>\d+)/$', PostCountHitDetailView.as_view(), name='post_detail'),

	# url(r'^pill_detail/(?P<pk>\d+)/$', PillDetailView.as_view(), name='pill_detail'),

]