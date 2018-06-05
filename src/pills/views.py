from django.views.generic import ListView

from .models import Pills


class PillListView(ListView):
	model = Pills
	template_name = "pills/pill_list.html"

	def get_context_data(self, **kwargs):
		context = super(PillListView, self).get_context_data(**kwargs)
		return context