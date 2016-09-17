from django import template
register = template.Library()
from django.contrib.auth.models import User
from ..models import Profile

@register.simple_tag
def new_profile(request):
	try:
		perfil = request.user.profile
		return False
	except:
		perfil = Profile()
		perfil.user = request.user
		perfil.save()
		return True
