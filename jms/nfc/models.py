from django.db import models
from django.utils.translation import gettext_lazy as _

class NFCTag(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"), null=False, blank=False)
    authority = models.CharField(max_length=100, verbose_name=_("authority"), null=False, blank=False)
    is_free = models.BooleanField(default=False, verbose_name=_("is free"), null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("NFC Tag")
        verbose_name_plural = _("NFC Tags")