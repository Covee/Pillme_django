from django.shortcuts import render

from hitcount.views import HitCountDetailView

from django.views.generic import DetailView, ListView
from .models import gPost


class gPostListView(ListView):
	model = gPost
	template_name = 'goodtoknow/post_list.html'


class gPostCountHitDetailView(HitCountDetailView):
    model = gPost        # your model goes here
    count_hit = True    # set to True if you want it to try and count the hit



# class gPostDetailView(DetailView):
# 	model = gPost
# 	template_name = 'goodtoknow/gpost_detail.html'

