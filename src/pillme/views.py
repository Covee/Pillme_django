# from django.contrib.auth import authenticate, login, get_user_model


from django.http import HttpResponse
from django.shortcuts import render, redirect


def home_view(request):
	return render(request, "home.html", {})