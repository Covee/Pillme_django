from django.db import models


class Categories_Body(models.Model):
	name	= models.CharField(max_length=20, null=False)


class Caregories_Gender(models.Model):
	name	= models.CharField(max_length=20, null=False)


class Pills(models.Model):
	name			= models.CharField(max_length=20, null=False)
	description		= models.TextField(max_length=2000)
	ingredient		= models.TextField(max_length=2000)
	category_body	= models.ManyToManyField(Categories_Body)
	category_gender	= models.ManyToManyField(Caregories_Gender)
	image			= models.ImageField(upload_to='upload_images/pills/%Y/%m/%d')

			










	# < example >
	# name: 오메가3
	# desc: 짱좋음
	# ingredient: 밀가루, 쌀, 고추장.  /  재료는 눌렀을때 재료에 대한 설명칸만 있으면 될 것 같다(사진 있으면 사진도)
	# category_body	/	신체부위. ex) 시력, 혈관, 간
	# category_Gender	/	성별 추천 영양제



	# 관련 추천 제품 보여주기.