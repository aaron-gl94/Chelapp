from django.contrib import admin
from .models import Product, Category, TypeProduct


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(TypeProduct)
