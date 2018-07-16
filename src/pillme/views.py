# from django.contrib.auth import authenticate, login, get_user_model

from django.http import HttpResponse
from django.shortcuts import render, redirect

from pills.models import Pills, Categories_Body


def home_view(request):
	queryset = Pills.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, "home.html", context)


def navbar(request):
	pill = Pills.objects.all()
	body = Categories_Body.objects.filter(category_body)
	context = {
		# 'object_list': body,
		'object_list': pill,
	}
	return render(request, 'base/navbar.html', context)