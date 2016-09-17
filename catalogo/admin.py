from django.contrib import admin
from .models import Product, Category, TypeProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name_product',
        'category',
        'type_product',
    )
    list_filter = ('category','type_product')
    search_fields = ('name_product','category','type_product')
    prepopulated_fields = {'slug':('name_product',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(TypeProduct)
