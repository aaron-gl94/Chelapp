from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Product, Category
from carrito.forms import CartAddProductForm
# Create your views here.

class ProductListView(View):
    def get(self, request, category=None):
        template_name = 'catalogo/list_product.html'
        products = Product.objects.all()
        tag = None
        if category:
            tag = Category.objects.get(name_category=category)
            products = Product.objects.all().filter(category=tag)
        #cat = Category.objects.all()
        context = {
            'products':products,
            #'tag':tag,
            #'cat':cat,
        }
        return render(request, template_name, context)

class ProductDetailView(View):
    def get(self, request, slug):
        template_name = 'catalogo/detail_product.html'
        product = get_object_or_404(Product, slug=slug)
        form=CartAddProductForm()

        context = {
            'product':product,
            'form':form
        }
        return render(request, template_name, context)
