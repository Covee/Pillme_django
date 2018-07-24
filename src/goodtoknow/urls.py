from django.shortcuts import render
from django.conf.urls import url, include

from . import views
from .views import gPostListView, gPostCountHitDetailView, gpost_like


urlpatterns = [
    url(r'^post_list/$', gPostListView.as_view(), name='post_list'),
	url(r'^(?P<pk>\d+)/$', gPostCountHitDetailView.as_view(), name='post_detail'),

	url(r'^like/$', views.gpost_like, name='gpost_like'),


	# url(r'^comment/new/$', views.comment_new, name='pill_comment_new'),
	# url(r'^(?P<pill_pk>\d+)/comment/(?P<pk>\d+)/delete/$', views.comment_delete, name='pill_comment_delete'),

	# url(r'^like/$', views.pill_like, name='pill_like'),

]