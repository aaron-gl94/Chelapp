from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^category/(?P<category>[\w-]+)/$', views.ProductListView.as_view(), name='list_filter'),
    url(r'^detalle/(?P<slug>[\w-]+)/$', views.ProductDetailView.as_view(), name='detalle'),
    url(r'^', views.ProductListView.as_view(), name='products'),

]
