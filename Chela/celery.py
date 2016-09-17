import os
from celery import Celery
from django.conf import settings

#Seteamos el módulo settings de Django para que trabaje con celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Chela.settings')

app = Celery('Chela')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

