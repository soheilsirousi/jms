from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from catalogue.models import Product
from catalogue.serializers import ProductRetrieveSerializer
from jms.utils import generate_response


class ProductRetrieveAPI(APIView):

    def get(self, request, pk, *args, **kwargs):
        product = Product.objects.filter(uuid=pk)

        if product.exists():
            product = product[0]
            serializer = ProductRetrieveSerializer(product)
            data = generate_response(success=True, content=serializer.data)
            return Response(data, status=status.HTTP_200_OK)

        data = generate_response(success=False, error="Product not found")
        return Response(data, status=status.HTTP_404_NOT_FOUND)