from django.contrib import admin
from .models import Profile

class UserPro(admin.ModelAdmin):
	list_display = ('user',)
	orderin = ('user',)
	search_fields = ('user',)
admin.site.register(Profile)