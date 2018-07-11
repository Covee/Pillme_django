from django.contrib import admin

from .models import Post, Introduce, LikePost


admin.site.register(Post)
admin.site.register(Introduce)
admin.site.register(LikePost)


