from rest_framework import serializers
from catalogue.models import Product


class ProductSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source="store.name", read_only=True)
    category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = ("uuid", "name", "store", "category", "image", "is_available")