from django.shortcuts import render
from django.conf.urls import url, include

from .views import PostCreateView, PostListView, PostDetailView, PostDeleteView, PostCountHitDetailView, PostUpdateView


urlpatterns = [
    # url(r'^$', HomeView.as_view(), name='home'),
	url(r'^create/$', PostCreateView.as_view(), name='post_create'),
	url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(), name='post_delete'),
	url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view(), name='post_update'),
    url(r'^$', PostListView.as_view(), name='post_list'),
	url(r'^(?P<pk>\d+)/$', PostCountHitDetailView.as_view(), name='post_detail'),

	# url(r'^pill_detail/(?P<pk>\d+)/$', PillDetailView.as_view(), name='pill_detail'),

]