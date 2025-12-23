from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models import CustomUser


class State(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    state = models.ForeignKey(State, null=False, blank=False, on_delete=models.CASCADE, related_name='cities')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")


class Store(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, verbose_name=_('Name'), null=False, blank=False)
    state = models.ForeignKey(State, null=False, blank=False, on_delete=models.RESTRICT, related_name='stores')
    city = models.ForeignKey(City, null=False, blank=False, on_delete=models.RESTRICT, related_name='stores')
    address = models.TextField(null=False, blank=False)
    phone1 = models.CharField(null=False, blank=False, max_length=11, verbose_name=_('Phone number 1'))
    phone2 = models.CharField(null=False, blank=False, max_length=11, verbose_name=_('Phone number 2'))
    image = models.ImageField(upload_to=f'images/store/{name}', null=False, blank=False)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StoreUser(models.Model):
    user = models.OneToOneField(CustomUser, null=False, blank=False, on_delete=models.RESTRICT, related_name='stores')
    store = models.ForeignKey(Store, null=False, blank=False, on_delete=models.RESTRICT, related_name='users')
    is_owner = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)

    @classmethod
    def check_user_permissions(cls, store, user):
        has_record = cls.objects.filter(store=store, user=user).exists()
        return has_record

    @classmethod
    def check_user_ownership(cls, store, user):
        has_record = cls.objects.filter(store=store, user=user).first()
        if not has_record:
            return False

        return has_record.is_owner

    @classmethod
    def get_user_store(cls, user):
        if user.is_authenticated:
            if obj := cls.objects.filter(user=user).first():
                return obj.store

        return None

