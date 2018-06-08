from django.shortcuts import render
from django.conf.urls import url, include

from .views import PillListView, PillDetailView


urlpatterns = [
    url(r'^pill_list/$', PillListView.as_view(), name='pill_list'),
	url(r'^pill_detail/(?P<pk>\d+)/$', PillDetailView.as_view(), name='pill_detail'),

]