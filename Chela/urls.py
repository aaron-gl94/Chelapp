from django.conf.urls import url, include
from django.contrib import admin
from main import views
from django.conf import settings
from accounts import urls as AccUrls

SOCIAL_AUTH_URL_NAMESPACE = 'social'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomeView.as_view(),name="home"),
    url(r'^accounts/', include(AccUrls)),
    url('',include('social.apps.django_app.urls',namespace="social")),
    url(
        regex=r'^media/(?P<path>.*)$',
        view='django.views.static.serve',
        kwargs={'document_root':settings.MEDIA_ROOT}),
]
