from django.urls import path

from catalogue.views import ProductRetrieveAPI

urlpatterns = [
    path("product/<uuid:pk>/", ProductRetrieveAPI.as_view(), name='product-retrieve'),
]