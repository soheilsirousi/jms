from django.contrib import admin
from nfc.models import NFCTag


@admin.register(NFCTag)
class NFCTagAdmin(admin.ModelAdmin):
    list_display = ("name", "authority", "is_free")

