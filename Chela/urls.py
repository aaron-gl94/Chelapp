from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from main import views
from accounts import urls as AccUrls
from catalogo import urls as CatalogoUrls
from django.views.generic import TemplateView
from django.contrib.auth.views import logout
from carrito import urls as cartUrls
from orders import urls as orderUrls
from paypal.standard.ipn import urls as paypalUrls
from payment import urls as paymentUrls

SOCIAL_AUTH_URL_NAMESPACE = 'social'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include(cartUrls, namespace="cart")),
    url(r'^$',views.HomeView.as_view(),name="home"),
    url(r'^nosotros/',views.AboutUsView.as_view(),name="nosotros"),
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
    url(r'^users/logout/$',logout,{'next_page': 'home'},name="user-logout"),
    url(r'^orders/', include(orderUrls, namespace="orders")),
    url(r'^paypal/', include(paypalUrls)),
    url(r'^payment/', include(paymentUrls,namespace='payment')),

]