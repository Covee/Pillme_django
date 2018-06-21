from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Profile


class SignupForm(forms.Form):
    email       = forms.EmailField(label=('Email'), widget=forms.EmailInput(attrs={'placeholder':('Email adress'),}))
    nickname    = forms.CharField(label=('닉네임'), required=True, widget=forms.TextInput(attrs={'placeholder':('닉네임'),}))

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.nickname = self.cleaned_data['nickname']
        user.save()

        profile = Profile()
        profile.user = user
        profile.email = self.cleaned_data['email']
        profile.nickname = self.cleaned_data['nickname']
        profile.save()