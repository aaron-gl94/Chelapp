from django.conf.urls import url, include
from django.contrib import admin
from main import views
from django.views.static import serve
from django.conf import settings
from catalogo import urls as CatalogoUrls
from django.contrib.auth.views import logout
from django.views.generic import TemplateView

SOCIAL_AUTH_URL_NAMESPACE = 'social'

urlpatterns = [
 
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomeView.as_view(),name="home"),
    url('',include('social.apps.django_app.urls',namespace="social")),

    url(
        r'^users/logout/$',
        logout,
        {'next_page': '/catalogo'},
        name="user-logout"),
    url(r'^$', TemplateView.as_view(template_name="base.html"), name="home"),
    url(r'^catalogo/', include(CatalogoUrls, namespace="catalogo")),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}),
]
