from django.db.models import Q

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required



from .models import Pills, Like
import json


class PillListView(ListView):
	model = Pills
	template_name = "pills/pill_list.html"

	def get_context_data(self, **kwargs):
		context = super(PillListView, self).get_context_data(**kwargs)
		return context

	def get_queryset(self, *args, **kwargs):
		qs = Pills.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
					Q(name__icontains=query)
				)
		return qs


class PillDetailView(DetailView):
	model = Pills
	template_name = 'pills/pill_detail.html'
	# context_object_name = 'pills'


@login_required
def pill_like(request, pk):
	pill = get_object_or_404(Pills, pk=pk)

	pill_like, pill_like_created = pill.like_set.get_or_create(user=request.user)

	if not pill_like_created:
		pill_like.delete()

	return redirect('pills:pill_list')