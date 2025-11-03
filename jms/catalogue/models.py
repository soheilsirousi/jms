from django.db import models
from store.models import Store


class ProductCategory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100, null=False, blank=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'images/store/{Store.name}/products/', null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name