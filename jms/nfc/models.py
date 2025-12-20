from django.db import models
from django.utils.translation import gettext_lazy as _

from catalogue.models import Product


class NFCTag(models.Model):
    number = models.PositiveIntegerField(verbose_name=_("number"), null=False, blank=False)
    serial_number = models.CharField(max_length=100, verbose_name=_("serial_number"), null=False, blank=False, unique=True)
    is_free = models.BooleanField(default=True, verbose_name=_("is free"), null=False, blank=False)

    def __str__(self):
        return f'Tag number: {self.number}'

    class Meta:
        verbose_name = _("NFC Tag")
        verbose_name_plural = _("NFC Tags")


class ProductTag(models.Model):
    tag = models.ForeignKey(NFCTag, on_delete=models.CASCADE, verbose_name=_("tag"), null=False, blank=False, related_name="products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"), null=False, blank=False, related_name="tags")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)