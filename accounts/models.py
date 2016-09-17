<<<<<<< HEAD
from django.db import models

# Create your models here.
=======
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	tel = models.CharField(max_length=10, blank=True, null=True)
	date_of_birth = models.DateField(blank=True,null=True)
	photo = models.ImageField(upload_to="users/%Y/%m/%d",blank=True)


	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user.username)
>>>>>>> 8bb5fbf91d28da8f14633e17358226754acfe26d
