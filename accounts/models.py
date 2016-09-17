from __future__ import unicode_literals
from django.db import models
from django.conf import settings


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,unique=True)
	tel = models.CharField(max_length=10, blank=True, null=True)
	date_of_birth = models.DateField(blank=True,null=True)
	photo = models.ImageField(upload_to="users/%Y/%m/%d",blank=True)

	def __str__(self):
		return self.user.username