from django.contrib import admin
from django.contrib.auth.decorators import login_required

from .models import Pills, Categories_Body, Categories_Gender, Like



admin.site.register(Pills)
admin.site.register(Categories_Body)
admin.site.register(Categories_Gender)

admin.site.login = login_required(admin.site.login)

class LikeInline(admin.TabularInline):
	model = Pills.like_user_set.through


class PillsAdmin(admin.ModelAdmin):
	list_display 	= '__all__'
	inlines			= [LikeInline,]


admin.site.register(Like)

class LikeAdmin(admin.ModelAdmin):
	list_display = ['id','pills','user','created_at']

	def get_actions(self, request):		# delete like
		actions = super().get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions




