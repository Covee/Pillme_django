from django.db import models
from django.core.urlresolvers import reverse

from PIL import Image


class Categories_Body(models.Model):
	name		= models.CharField(max_length=20, null=False)
	description	= models.TextField(max_length=2000)

	def __str__(self):
		return self.name


class Categories_Gender(models.Model):
	name	= models.CharField(max_length=20, null=False)

	def __str__(self):
		return self.name


class Pills(models.Model):
	name			= models.CharField(max_length=20, null=False)
	feature			= models.TextField(max_length=50, null=True)
	editor_said		= models.TextField(max_length=50, null=True)
	description		= models.TextField(max_length=2000)
	ingredient		= models.TextField(max_length=2000)
	category_body	= models.ManyToManyField(Categories_Body)
	category_gender	= models.ManyToManyField(Categories_Gender)
	image			= models.ImageField(upload_to='upload_images/pills/%Y/%m/%d')

	def __str__(self):
		return self.name
			
	def get_absolute_url(self):
		return reverse('pills:pill_detail', args=[self.id])









	# < example >
	# name: 오메가3
	# desc: 짱좋음
	# ingredient: 밀가루, 쌀, 고추장.  /  재료는 눌렀을때 재료에 대한 설명칸만 있으면 될 것 같다(사진 있으면 사진도).  요거를...어디서 추출하는지를 쓰는게 더 좋으려나
	# category_body	/	신체부위. ex) 시력, 혈관, 간
	# category_Gender	/	성별 추천 영양제
	# 복용시 주의사항, 복용법, 관련정보, 추천 링크 등 필요함
	# 의견(코멘트)
	# 하트(얼마나 이 영양제를 추천하는가? 인스타그램 좋아요 같은 것 필요)
	# 관련 추천 제품 보여주기.



	
	# 파일 저장되는 경로 설정 어떻게 할지 구체적으로 생각 해보기.