from django.shortcuts import render
from django.conf.urls import url, include

from .views import PillListView


urlpatterns = [
    url(r'^$', PillListView.as_view(), name='pill_list'),
    
]