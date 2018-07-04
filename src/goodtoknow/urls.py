from django.shortcuts import render
from django.conf.urls import url, include

from .views import gPostListView, gPostDetailView


urlpatterns = [
    url(r'^post_list/$', gPostListView.as_view(), name='post_list'),
	url(r'^post_detail/(?P<pk>\d+)/$', gPostDetailView.as_view(), name='post_detail'),
	# url(r'^comment/new/$', views.comment_new, name='pill_comment_new'),
	# url(r'^(?P<pill_pk>\d+)/comment/(?P<pk>\d+)/delete/$', views.comment_delete, name='pill_comment_delete'),

	# url(r'^like/$', views.pill_like, name='pill_like'),

]