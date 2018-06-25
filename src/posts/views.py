from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Post


# class HomeView(TemplateView):
# 	model = Post
# 	template_name = 'posts/freeboard.html'


class PostListView(ListView):
	model = Post
	template_name = 'posts/post_list.html'