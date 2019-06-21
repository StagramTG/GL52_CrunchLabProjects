from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status

from ..models import User
from ..serializers import UserSerializer


@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def users_search(request, username):
    users = User.objects.filter(username__icontains=username)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_details(request):
    serializer = UserSerializer(request.user)
    return Response(data=serializer.data)


@api_view(['POST'])
def user_selfupdate(request):
    """ Update himself, use another method to update others """
    username = request.data['username']
    email = request.data['email']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    phone = request.data['phone']
    location = request.data['location']

    if email and first_name and last_name:
        # Update
        user = request.user
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.phone = phone
        user.location = location

        user.save()
        return Response({}, status=status.HTTP_200_OK)
    else:
        # No update + return code 400
        return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_update(request, id):
    """ Update himself, use another method to update others """
    username = request.data['username']
    email = request.data['email']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    phone = request.data['phone']
    location = request.data['location']

    if email and first_name and last_name:
        # Update
        user = User.objects.get(pk=id)
        if user:
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone = phone
            user.location = location

            user.save()
            return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_info(request, id):
    user = User.objects.filter(pk=id)
    serializer = UserSerializer(user, many=True)
    return Response(data=serializer.data[0])


@api_view(['POST'])
def user_delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return Response({}, status=status.HTTP_200_OK)
