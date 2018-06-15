# from django.contrib.auth import authenticate, login, get_user_model


from django.http import HttpResponse
from django.shortcuts import render, redirect

from pills.models import Pills


def home_view(request):
	queryset = Pills.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, "home.html", context)