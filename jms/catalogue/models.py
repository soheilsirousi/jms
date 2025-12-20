from django.db import models
from uuid import uuid4
from catalogue.utils import product_image_upload_path
from store.models import Store


class ProductCategory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100, null=False, blank=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "product category"
        verbose_name_plural = "product categories"

class Product(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_upload_path, null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name