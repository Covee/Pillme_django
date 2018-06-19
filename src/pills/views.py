from django.db.models import Q

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.views.decorators.http import require_POST

from .models import Pills, Like, Comment
from .forms import CommentForm
import json


class PillListView(ListView):
	model = Pills
	template_name = "pills/pill_list.html"
	form_class = CommentForm

	def get_context_data(self, **kwargs):
		context = super(PillListView, self).get_context_data(**kwargs)
		return context

	def get_queryset(self, *args, **kwargs):
		qs = Pills.objects.prefetch_related('category_body','category_gender','like_user_set').all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
					Q(name__icontains=query)
				)
		return qs


@login_required
def comment_new(request, pk):
	pill = get_object_or_404(Pills, pk=pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = request.user
			comment.pills = pill
			comment.save()
			return redirect("pills:pill_list")
	return render(request, "pills/pill_list.html", {'form':form})


class PillDetailView(DetailView):
	model = Pills
	template_name = 'pills/pill_detail.html'
	# context_object_name = 'pills'


@login_required
@require_POST	# POST method만 받음
def pill_like(request):
	pk = request.POST.get('pk', None)
	pill = get_object_or_404(Pills, pk=pk)

	pill_like, pill_like_created = pill.like_set.get_or_create(user=request.user)

	if not pill_like_created:
		pill_like.delete()
		message = "좋아요 취소"
	else:
		message = "좋아요"

	context = {
				'like_count': pill.like_count,
				'message': message,
				'username': request.user.username
	}

	return HttpResponse(json.dumps(context))









