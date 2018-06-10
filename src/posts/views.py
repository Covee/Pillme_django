from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Post


class HomeView(TemplateView):
	model = Post
	template_name = 'posts/freeboard.html'