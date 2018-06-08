from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegistrationForm(forms.Form):
	username	= forms.CharField(label='아이디 ', min_length=6, max_length=20, widget= forms.TextInput
                           (attrs={'placeholder':'4-20자 사이로'}))
	email		= forms.EmailField(label='이메일 ', widget= forms.EmailInput
                           (attrs={'placeholder':'이메일 입력'}))
	password1	= forms.CharField(label='비밀번호 ', min_length=8, max_length=20, widget=forms.PasswordInput
							(attrs={'placeholder':'8-20자 사이'}))
	password2	= forms.CharField(label='비밀번호 확인 ', min_length=8, max_length=20, widget=forms.PasswordInput
							(attrs={'placeholder':'8-20자 사이'}))


	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError("패스워드가 일치하지 않습니다.")
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
