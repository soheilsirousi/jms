from rest_framework import serializers

from store.models import Store


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('uuid', 'name', 'state', 'city', 'phone1', 'phone2', 'is_available', 'is_active')