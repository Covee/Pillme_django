from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegistrationForm(forms.Form):
	username	= forms.CharField()
	email		= forms.EmailField()
	password1	= forms.CharField(label='비밀번호', widget=forms.PasswordInput)
	password2	= forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise ValidationError("패스워드가 일치하지 않습니다.")
		return password2

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username__icontains=username).exists():
			raise forms.ValidationError("사용중인 아이디입니다.")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email__icontains=email).exists():
			raise forms.ValidationError("사용중인 이메일입니다.")
		return email
