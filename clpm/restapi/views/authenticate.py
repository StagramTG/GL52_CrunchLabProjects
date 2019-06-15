from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework import status

from django.contrib.auth import authenticate, login
from django.conf import settings
from ..serializers import UserSerializer


class AuthView(viewsets.ViewSet):
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = ()

    def login(self, request, *args, **kwargs):
        # authenticate the user
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user:
            # success
            login(request, user)
            response = Response({'username': user.username, 'session': request.session}, status=status.HTTP_200_OK)
            return response
        else:
            # failure
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)