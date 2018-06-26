from django.shortcuts import render


from hitcount.views import HitCountDetailView

from django.views.generic import TemplateView, ListView, DetailView

from .models import Post


# class HomeView(TemplateView):
# 	model = Post
# 	template_name = 'posts/freeboard.html'


class PostListView(ListView):
	model = Post
	template_name = 'posts/post_list.html'


class PostDetailView(DetailView):
	model = Post
	
	# template_name = 'posts/post_detail.html'


class PostMixinDetailView(object):
	model = Post

	def get_context_data(self, **kwargs):
		context = super(PostMixinDetailView, self).get_context_data(**kwargs)
		context['post_list'] = Post.objects.all()[:5]
		context['post_views'] = ["ajax", "detail", "detail-with-count"]
		return context


# class PostDetailJSONView(PostMixinDetailView, DetailView):
#     template_name = 'posts/post_ajax.html'

#     @classmethod
#     def as_view(cls, **initkwargs):
#         view = super(PostDetailJSONView, cls).as_view(**initkwargs)
#         return ensure_csrf_cookie(view)


# class PostDetailView(PostMixinDetailView, HitCountDetailView):
#     # Generic hitcount class based view.
#     pass


class PostCountHitDetailView(HitCountDetailView):
    model = Post        # your model goes here
    count_hit = True    # set to True if you want it to try and count the hit

