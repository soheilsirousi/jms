from django.contrib import admin
from catalogue.models import ProductCategory, Product


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("store", "name", "is_available")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("store", "name", "category", "is_available")
