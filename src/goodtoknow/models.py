from django.conf import settings

from django.db import models

from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin


class gPost(models.Model, HitCountMixin):
	title		= models.CharField(max_length=50, blank=False)
	content		= models.TextField(max_length=20000, blank=False, null=False)
	files		= models.FileField(null=True, blank=True, upload_to='upload_images/goodtoknow/%Y/%m')
	images		= models.ImageField(null=True, blank=True, upload_to='upload_images/goodtoknow/%Y/%m')
	timestamp 	= models.DateTimeField(auto_now_add=True)
	hit_count 	= GenericRelation(HitCount, object_id_field='object_pk', 
											related_query_name='hit_count_generic_relation')
	likes 		= models.ManyToManyField(settings.AUTH_USER_MODEL,
												blank=True,
												related_name='like_gpost',
												through='LikegPost')

	# comments

	class Meta:
		ordering = ['-id']

	def __str__(self):
		return self.title

	@property
	def like_count(self):
		return self.likes.count()


class LikegPost(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL)
	gpost 		= models.ForeignKey(gPost)
	created_at	= models.DateTimeField(auto_now_add=True)
	updated_at	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return [self.gpost, self.user]