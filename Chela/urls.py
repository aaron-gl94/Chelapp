from django.conf.urls import url, include
from django.contrib import admin
from main import views
from django.conf import settings
from accounts import urls as AccUrls
from catalogo import urls as CatalogoUrls
from django.views.static import serve
from django.views.generic import TemplateView
from django.contrib.auth.views import logout
from carrito import urls as cartUrls

SOCIAL_AUTH_URL_NAMESPACE = 'social'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include(cartUrls, namespace="cart")),
    url(r'^$',views.HomeView.as_view(),name="home"),
    url(r'^accounts/', include(AccUrls)),
    url('',include('social.apps.django_app.urls',namespace="social")),
    url(r'^catalogo/', include(CatalogoUrls, namespace="catalogo")),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}),

    # Home URL
    url(r'^$', TemplateView.as_view(template_name="base.html"), name="home"),
    # Logout URL
    url(
        r'^users/logout/$',
        logout,
        {'next_page': '/catalogo'},
        name="user-logout"),

]
