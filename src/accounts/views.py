from django.contrib.auth import get_user_model

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from django.core.urlresolvers import reverse_lazy   # generic view 에서는 reverse_lazy 사용한다고 함


User = get_user_model()


class UserDetailView(DetailView):
	template_name = 'accounts/user_detail.html'
	queryset = User.objects.all()

	def get_object(self):
		return get_object_or_404(
			User,
			username__iexact=self.kwargs.get("username")
			)