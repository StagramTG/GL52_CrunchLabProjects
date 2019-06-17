from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from ..serializers import ProjectSerializer
from ..models import Project


@api_view(['GET'])
def project_details(request, id):
    """ Get details for the given project """
    pass


@api_view(['GET'])
def project_list(request):
    """ Get a list of all existing projects """
    pass


@api_view(['GET'])
def project_user_list(request, userid):
    """ Get specified user's projects list """
    pass