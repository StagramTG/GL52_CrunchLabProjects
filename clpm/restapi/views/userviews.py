from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from ..models import User
from ..serializers import UserSerializer


@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def user_details(request):
    serializer = UserSerializer(request.user)
    return Response(data=serializer.data)