from django.conf import settings
from django.db import models



class Profile(models.Model):
	user 		= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	email 		= models.EmailField()
	nickname 	= models.CharField(max_length=14)

	class Meta:
		db_table = 'account_profile'
		app_label = 'account' 	# account 앱 카테고리에서 관리되게 함

	def __str__(self):
		return self.nickname, self.email