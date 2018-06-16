from django.contrib import admin

from .models import Pills, Categories_Body, Categories_Gender, Like



admin.site.register(Pills)
admin.site.register(Categories_Body)
admin.site.register(Categories_Gender)



class LikeInline(admin.TabularInline):
	model = Pills.like_user_set.through


class PillsAdmin(admin.ModelAdmin):
	list_display 	= '__all__'
	inlines			= [LikeInline,]


admin.site.register(Like)

class LikeAdmin(admin.ModelAdmin):
	list_display = ['id','pills','user','created_at']