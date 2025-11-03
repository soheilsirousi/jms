from django.contrib import admin
from store.models import State, Store, City, StoreUser


class StoreUserInline(admin.StackedInline):
    model = StoreUser

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("name", "is_available")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state", "is_available")


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "state", "city", "phone1", "phone2", "is_available", "is_active")
    inlines = [StoreUserInline, ]