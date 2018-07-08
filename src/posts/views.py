from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy

from hitcount.views import HitCountDetailView

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, FormView, UpdateView

from .models import Post, Introduce
from .forms import PostCreateForm
import json



# class HomeView(TemplateView):
# 	model = Post
# 	template_name = 'posts/freeboard.html'


class PostCreateView(CreateView):
	form_class = PostCreateForm
	success_url 	= reverse_lazy('freeboard:post_list')
	template_name 	= 'posts/post_create.html'

	def get_initial(self):
		return {
				"author": self.request.user
				}


class PostDeleteView(DeleteView):
	model = Post
	template_name = 'posts/post_delete.html'
	success_url = reverse_lazy('freeboard:post_list')
	

class PostListView(ListView):
	model = Post
	template_name = 'posts/post_list.html'


class PostDetailView(DetailView):
	model = Post

	# template_name = 'posts/post_detail.html'


class PostUpdateView(UpdateView):
	model = Post
	success_url 	= reverse_lazy('freeboard:post_list')
	template_name 	= 'posts/post_create.html'
	fields 			= ['title', 'content', 'images', 'files',]



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



@login_required
@require_POST	# POST method만 받음
def post_like(request):
	pk = request.POST.get('pk', None)
	post = get_object_or_404(Post, pk=pk)

	post_like, post_like_created = post.likepost_set.get_or_create(user=request.user)

	if not post_like_created:
		post_like.delete()
		message = "좋아요 취소"
	else:
		message = "좋아요"

	context = {
				'like_count': post.like_count,
				'message': message,
				'username': request.user.username
	}

	return HttpResponse(json.dumps(context))



class IntroduceView(DetailView):
	model = Introduce
	template_name = 'posts/introduce.html'


