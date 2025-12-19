from django.db.models.signals import post_save
from django.dispatch import receiver
from nfc.models import ProductTag


@receiver(post_save, sender=ProductTag)
def change_nfc_is_free(sender, instance, created, **kwargs):
    if created:
        instance.tag.is_free = False
        instance.tag.save()
