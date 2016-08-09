from django.conf.urls import url
from django.contrib import admin
from main import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomeView.as_view(),name="home"),
]
