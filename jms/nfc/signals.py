from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from nfc.models import ProductTag


@receiver(post_save, sender=ProductTag)
def occupy_nfc(sender, instance, created, **kwargs):
    if created:
        instance.tag.is_free = False
        instance.tag.save()


@receiver(post_delete, sender=ProductTag)
def free_nfc(sender, instance, **kwargs):
    instance.tag.is_free = True
    instance.tag.save()