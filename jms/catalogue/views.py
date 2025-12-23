from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from catalogue.models import Product
from catalogue.serializers import ProductSerializer
from jms.utils import generate_response


class ProductRetrieveAPI(APIView):

    def get(self, request, store_pk, product_pk, *args, **kwargs):
        product = Product.objects.select_related("store").filter(uuid=product_pk, store__uuid=store_pk)

        if product.exists():
            product = product[0]
            serializer = ProductSerializer(product)
            data = generate_response(success=True, content=serializer.data)
            return Response(data, status=status.HTTP_200_OK)

        data = generate_response(success=False, error="Product not found")
        return Response(data, status=status.HTTP_404_NOT_FOUND)


class ProductListAPI(APIView):

    def get(self, request, store_pk, *args, **kwargs):
        products = Product.objects.select_related("store").filter(store__uuid=store_pk)

        if products.exists():
            serializer = ProductSerializer(products, many=True)
            data = generate_response(success=True, content=serializer.data)
            return Response(data, status=status.HTTP_200_OK)

        data = generate_response(success=False, error="product list is empty.")
        return Response(data, status=status.HTTP_404_NOT_FOUND)