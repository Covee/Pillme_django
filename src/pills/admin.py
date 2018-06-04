from django.contrib import admin

from .models import Pills, Categories_Body, Categories_Gender


admin.site.register(Pills)
admin.site.register(Categories_Body)
admin.site.register(Categories_Gender)