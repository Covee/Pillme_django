from django.conf import settings

from django.db import models


class Post(models.Model):
	title		= models.CharField(max_length=50, blank=False)
	author		= models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False)
	content		= models.TextField(max_length=5000, blank=False, null=False)
	files		= models.FileField(null=True, blank=True)
	images		= models.ImageField(null=True, blank=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)

	# comments
	# likes

	class Meta:
		ordering = ['-id']

	def __str__(self):
		return self.title


	