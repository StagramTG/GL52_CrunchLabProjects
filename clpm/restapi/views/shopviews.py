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
