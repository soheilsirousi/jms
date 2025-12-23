from django.urls import path

from catalogue.views import ProductRetrieveAPI, ProductListAPI

urlpatterns = [
    path("store/<uuid:store_pk>/product/list/", ProductListAPI.as_view(), name='product-list'),
    path("store/<uuid:store_pk>/product/<uuid:product_pk>/", ProductRetrieveAPI.as_view(), name='product-retrieve'),
]