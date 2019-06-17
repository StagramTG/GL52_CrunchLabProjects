from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from ..models import User, Account
from ..serializers import UserSerializer


class LoginView(viewsets.ViewSet):
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
            serializer = UserSerializer(user)
            response = Response(serializer.data, status=status.HTTP_200_OK)
            return response
        else:
            # failure
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(viewsets.ViewSet):
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = ()

    
    def logout(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(viewsets.ViewSet):
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated)

    def register(self, request, *args, **kwargs):
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password = request.data['password']
        
        if email & password:
            # Create new user
            user = User.objects.create_user(
                username=first_name[0]+last_name, 
                email=email, 
                password=password
            )
            user.first_name = first_name
            user.last_name = last_name

            # Create user's wallet
            wallet = Account()
            wallet.name = wallet.id + '_' + first_name + '_' + last_name + '_ACCOUNT'
            wallet.save()
            user.account_id = wallet

            user.save()
            return Response({}, status=status.HTTP_200_OK)
        
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
