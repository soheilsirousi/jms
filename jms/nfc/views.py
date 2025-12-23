from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from catalogue.models import Product
from jms.utils import generate_response
from nfc.models import NFCTag, ProductTag
from nfc.serializers import TagSerializer
from store.models import StoreUser


class TagScanAPIView(APIView):

    def get(self, request, serial_number, *args, **kwargs):
        store = StoreUser.get_user_store(request.user)
        tag = NFCTag.objects.filter(serial_number=serial_number).first()

        if tag:
            product_tag = ProductTag.objects.select_related("product").filter(tag=tag).first()
            if product_tag:
                return redirect("product-retrieve", store_pk=product_tag.product.store.uuid, product_pk=product_tag.product.uuid)
            else:
                if tag.store == store:
                    return redirect("assign-product", serial_number=serial_number)
                else:
                    data = generate_response(success=False, error="No product assigned to this tag.")
                    return Response(data, status=status.HTTP_404_NOT_FOUND)
        else:
            if store:
                tag = NFCTag.objects.create(serial_number=serial_number, store=store)
                return redirect("assign-product", serial_number=serial_number)
            else:
                data = generate_response(success=False, error="This tag does not exist.")
                return Response(data, status=status.HTTP_404_NOT_FOUND)



class AssignProductAPI(APIView):

    def post(self, request, serial_number, *args, **kwargs):
        tag = NFCTag.objects.filter(serial_number=serial_number).first()
        if not tag:
            response = generate_response(success=False, error="This tag does not exist.\n you must register first.")
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        store = StoreUser.get_user_store(request.user)

        if tag.store != store:
            response = generate_response(success=False, error="Permission denied.")
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        data = request.data
        product_uuid = data.get('product_uuid')
        if not product_uuid:
            response = generate_response(success=False, error="Can not find product in payload")
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.filter(uuid=product_uuid).first()
        if not product:
            response = generate_response(success=False, error="Product not found")
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        prev_product_tag = ProductTag.objects.filter(tag=tag).first()
        if prev_product_tag:
            prev_product_tag.delete()

        product_tag = ProductTag.objects.create(tag=tag, product=product)
        response = generate_response(success=True, content="Product assigned to this tag.")
        return Response(response, status=status.HTTP_200_OK)


class DeleteTagAPI(APIView):

    def get(self, request, serial_number, *args, **kwargs):
        tag = NFCTag.objects.filter(serial_number=serial_number).first()
        if not tag:
            response = generate_response(success=False, error="Tag does not exist.")
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        store = StoreUser.get_user_store(request.user)

        if tag.store != store:
            response = generate_response(success=False, error="Permission denied.")
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        product_tag = ProductTag.objects.filter(tag=tag).first()
        if product_tag:
            response = generate_response(success=False, error="This tag is assigned to the product.\n you must first unlink product from tag.")
            return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

        tag.delete()
        response = generate_response(success=True, content="Tag deleted.")
        return Response(response, status=status.HTTP_200_OK)


class RemoveProductTagAPI(APIView):

    def get(self, request, serial_number, *args, **kwargs):
        tag = NFCTag.objects.filter(serial_number=serial_number).first()
        if not tag:
            response = generate_response(success=False, error="Tag does not exist.")
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        store = StoreUser.get_user_store(request.user)

        if tag.store != store:
            response = generate_response(success=False, error="Permission denied.")
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        product_tag = ProductTag.objects.filter(tag=tag).first()
        if not product_tag:
            response = generate_response(success=False, error="No product assigned to this tag.")
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        product_tag.delete()
        response = generate_response(success=True, content="Product tag deleted.")
        return Response(response, status=status.HTTP_200_OK)


class TagRetrieveAPI(APIView):

    def get(self, request, serial_number, *args, **kwargs):
        tag = NFCTag.objects.filter(serial_number=serial_number).first()
        if not tag:
            response = generate_response(success=False, error="Tag does not exist.")
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        serializer = TagSerializer(tag)
        response = generate_response(success=True, content=serializer.data)
        return Response(response, status=status.HTTP_200_OK)

