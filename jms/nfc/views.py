from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from jms.utils import generate_response
from nfc.models import NFCTag


class TagInitAPIView(APIView):

    def get(self, request, serial_number, *args, **kwargs):
        tags = NFCTag.objects.filter(serial_number=serial_number)

        if tags.exists():
            data = generate_response(success=True, content="tag already exists.")
            return Response(data, status=status.HTTP_204_NO_CONTENT)

        tag = NFCTag.objects.create(serial_number=serial_number)
        data = generate_response(success=True, content="tag created.")
        return Response(data, status=status.HTTP_201_CREATED)