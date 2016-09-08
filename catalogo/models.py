from django.db import models



class TypeProduct(models.Model):
    name_subcategory = models.CharField(max_length=50)

    def __str__(self):
        return self.name_subcategory
        
class Category(models.Model):
    name_category = models.CharField(max_length=50)
    type_product = models.ManyToManyField(TypeProduct, related_name='type_product')

    def __str__(self):
        return self.name_category

class Product(models.Model):
    COUNTRY_CHOICE = (
        ('Mexico','México'),
        ('Francia','Francia'),
        ('Italia','Italia'),
        ('NuevaZelanda','Nueva Zelanda'),
        ('Chile','Chile'),
        ('Portugal','Portugal'),
        ('Espana','España'),
        ('Alemania','Alemania'),
    )
    name_product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='category')
    description = models.TextField()
    picture = models.ImageField(upload_to='products')
    type_product = models.ForeignKey(TypeProduct, related_name='type_drink')
    available = models.BooleanField(default=False)
    presentacion = models.CharField(max_length=30)
    country = models.CharField(max_length=10,choices=COUNTRY_CHOICE, blank=True, null=True)

    def __str__(self):
        return self.name_product
