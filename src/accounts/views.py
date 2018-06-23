from django.contrib.auth import get_user_model

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, FormView, TemplateView

from .forms import UserRegistrationForm
from django.core.urlresolvers import reverse_lazy   # generic view 에서는 reverse_lazy 사용한다고 함


User = get_user_model()


class UserDetailView(DetailView):
	model = User
	template_name = 'accounts/user_detail.html'


	# template_name = 'accounts/user_profile.html'
	# queryset = User.objects.all()

	# def get_object(self):
	# 	return get_object_or_404(
	# 		User,
	# 		username__iexact=self.kwargs.get("username")
	# 		)



# class UserRegisterView(FormView):
# 	template_name = 'accounts/user_register_form.html'
# 	form_class = UserRegistrationForm
# 	success_url = '/'

# 	def form_valid(self, form):
# 		username = form.cleaned_data.get('username')
# 		email	 = form.cleaned_data.get('email')
# 		password = form.cleaned_data.get('password')
# 		new_user = User.objects.create(username=username, email=email)
# 		new_user.set_password(password)
# 		new_user.save()
# 		return super(UserRegisterView, self).form_valid(form)