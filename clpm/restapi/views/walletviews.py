from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from ..serializers import AccountSerializer
from ..models import User, Account


@api_view(['GET'])
def account_details(request, id):
    """ Get account details for the given user"""
    account = Account.objects.get(id=id)

    if account:
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def account_supply(request):
    """ Update balance for the given user"""

    id = request.data['id']
    balance = float(request.data['amount'])

    account = Account.objects.get(id=id)

    if account:
        account.balance += balance

        account.save()
        return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)
