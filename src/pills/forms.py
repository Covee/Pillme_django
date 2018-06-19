from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.TextInput(attrs={
														'size': '60px',
														'placeholder': '댓글 달기',
														}))

	class Meta:
		model 	= Comment
		fields 	= ['content']