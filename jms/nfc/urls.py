from django.urls import path

from nfc.views import TagInitAPIView

urlpatterns = [
    path("init/<str:serial_number>/", TagInitAPIView.as_view(), name="init-tag"),
]