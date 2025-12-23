from django.urls import path

from nfc.views import TagScanAPIView, AssignProductAPI, DeleteTagAPI, RemoveProductTagAPI, TagRetrieveAPI

urlpatterns = [
    path("scan/<str:serial_number>/", TagScanAPIView.as_view(), name="scan-tag"),
    path("assign/<str:serial_number>/", AssignProductAPI.as_view(), name="assign-product"),
    path("delete/<str:serial_number>/", DeleteTagAPI.as_view(), name="delete-tag"),
    path("/<str:serial_number>/remove/", RemoveProductTagAPI.as_view(), name="remove-product-tag"),
    path("/<str:serial_number>/", TagRetrieveAPI.as_view(), name="tag-retrieve"),
]