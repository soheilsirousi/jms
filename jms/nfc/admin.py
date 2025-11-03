from django.contrib import admin
from nfc.models import NFCTag, ProductTag


@admin.register(NFCTag)
class NFCTagAdmin(admin.ModelAdmin):
    list_display = ("name", "authority", "is_free")


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ("product", "tag")
