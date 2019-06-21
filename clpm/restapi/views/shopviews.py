from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from ..serializers import ShopProductSerializer
from ..models import ShopProduct


@api_view(['GET'])
def product_list(request):
    products = ShopProduct.objects.all()
    serializer = ShopProductSerializer(products, many=True)
    return Response(data=serializer.data)

@api_view(['POST'])
def create_product(request):
    name = request.data['name']
    price = request.data['price']
    description = request.data['description']

    if name and price and description:
        product = ShopProduct.objects.create(
            name=name,
            price=price,
            description=description,
        )

        if product :
            product.save()
            return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def product_details(request, id):
    product = ShopProduct.objects.get(id=id)

    if product:
        serializer = ShopProductSerializer(product)
        return Response(data=serializer.data)

    return Response({})


@api_view(['POST'])
def product_delete(request, id):
    product = ShopProduct.objects.get(id=id)

    if product:
        product.delete()
        return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def product_update(request, id):
    name = request.data['name']
    price = request.data['price']
    description = request.data['description']

    if name and price and description:
        product = ShopProduct.objects.get(id=id)

        if product:
            product.name = name
            product.price = price
            product.description = description

            product.save()
            return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)
