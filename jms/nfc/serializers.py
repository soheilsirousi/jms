from packaging.tags import Tag
from rest_framework import serializers

from catalogue.serializers import ProductSerializer
from nfc.models import ProductTag


class TagSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source='tag.store.name', read_only=True)
    product = serializers.SerializerMethodField()

    def get_product(self, obj):
        product_tag = ProductTag.objects.filter(tag=obj)
        if not product_tag:
            return None

        serializer = ProductSerializer(product_tag.first().product)
        return serializer.data

    class Meta:
        model = Tag
        fields = ('serial_number', 'store', 'is_free', 'product')