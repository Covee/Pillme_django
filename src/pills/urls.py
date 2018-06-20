from django.shortcuts import render
from django.conf.urls import url, include

from . import views
from .views import PillListView, PillDetailView, pill_like, comment_new


urlpatterns = [
    url(r'^pill_list/$', PillListView.as_view(), name='pill_list'),
	url(r'^pill_detail/(?P<pk>\d+)/$', PillDetailView.as_view(), name='pill_detail'),
	url(r'^(?P<pill_pk>\d+)/comment/new/$', views.comment_new, name='pill_comment'),
	url(r'^(?P<pill_pk>\d+)/comment/(?P<pk>\d+)/delete/$', views.comment_delete, name='pill_comment_delete'),

	url(r'^like/$', views.pill_like, name='pill_like'),

]