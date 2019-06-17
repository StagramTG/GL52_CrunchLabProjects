from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from ..serializers import ProjectSerializer
from ..models import Project, User, Account


@api_view(['GET'])
def project_details(request, id):
    """ Get details for the given project """
    project = Project.objects.get(id=id)

    if project:
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def project_list(request):
    """ Get a list of all existing projects """
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def project_user_list(request, userid):
    """ Get specified user's projects list """
    pass


@api_view(['POST'])
def project_create(request):
    """ Create a new project from post data """
    name = request.data['name']
    description = request.data['description']

    if name and description:
        project = Project()
        project.name = name
        project.description = description
        project.user_id = request.user

        account = Account()
        account.balance = 0
        account.name = name + '_' + request.user.username + '_ACCOUNT'
        account.save()

        project.account_id = account
        project.save()

        return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def project_update(request):
    """ Update a project from post data """
    id = request.data['id']
    name = request.data['name']
    description = request.data['description']

    if name and description and id:
        project = Project.objects.get(id=id)

        if project:
            project.name = name
            project.description = description
            project.save()
            return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def project_delete(request):
    """ Delete a project from post data """
    id = request.data['id']

    if id:
        project = Project.objects.get(id=id)

        if project:
            project.delete()
            return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)