from django.shortcuts import render
from django.conf.urls import url, include

from . import views
from .views import PillListView, PillDetailView, pill_like


urlpatterns = [
    url(r'^pill_list/$', PillListView.as_view(), name='pill_list'),
	url(r'^pill_detail/(?P<pk>\d+)/$', PillDetailView.as_view(), name='pill_detail'),
	url(r'^pill_list/(?P<pk>\d+)/like/$', views.pill_like, name='pill_like'),

]