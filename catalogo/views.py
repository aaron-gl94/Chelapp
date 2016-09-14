from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Product
# Create your views here.

class ProductListView(View):
    def get(self, request):
        template_name = 'catalogo/list_product.html'
        products = Product.objects.all()
        context = {
            'products':products,
        }
        return render(request, template_name, context)

class ProductDetailView(View):
    def get(self, request, slug):
        template_name = 'catalogo/detail_product.html'
        product = get_object_or_404(Product, slug=slug)
        context = {
            'product':product,
        }
        return render(request, template_name, context)
