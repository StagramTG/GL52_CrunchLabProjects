from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from datetime import date

from ..serializers import AccountSerializer, AccountTransactionSerializer
from ..models import Account, AccountTransaction, AccountReload


@api_view(['GET'])
def account_details(request, id):
    """ Get account details for the given user"""
    account = Account.objects.get(id=id)

    if account:
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def account_transaction(request):
    """Update history of transaction"""
    id = request.data['id']
    amount = float(request.data['amount'])

    transaction = AccountTransaction.objects.create(
        amount=amount,
        created_at=date.today(),
        account_id=Account.objects.get(id=id),
    )

    if transaction :
        transaction.save()
        return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def account_reload(request):
    """Update balance for the given user"""
    id = request.data['id']
    amount = float(request.data['amount'])

    reload = AccountReload.objects.create(
        amount= amount,
        created_at=date.today(),
        account_id= Account.objects.get(id=id),
    )

    transaction = AccountTransaction.objects.create(
        amount=amount,
        created_at=date.today(),
        account_id=Account.objects.get(id=id),
    )
    
    if reload and transaction:
        reload.save()
        transaction.save()
        return Response({}, status=status.HTTP_200_OK)

    """
    account_transaction(request)

    if reload :
        reload.save()
        return Response({}, status=status.HTTP_200_OK)

    """

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


@api_view(['GET'])
def transaction_list(request, id):
    """Get the list of user's transaction"""
    transactions = AccountTransaction.objects.filter(account_id=Account.objects.get(id=id)).order_by('-created_at')[:5]

    if transactions:
        serializer = AccountTransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)
