from django.db.models import Q

from django.views.generic import ListView, DetailView

from .models import Pills


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