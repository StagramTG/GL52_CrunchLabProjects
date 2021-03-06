from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from ..serializers import ProjectSerializer, ProjectRolesSerializer, UserProjectSerializer
from ..models import Project, User, Account, ProjectRoles, UserProject


# ==========================================================
#       PROJECT API
# ==========================================================


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
        account.name = name.replace(' ', '_') + '_' + request.user.username + '_ACCOUNT'
        account.save()

        project.account_id = account
        project.save()

        # User role 'Créateur'
        userproject = UserProject()
        userproject.user_id = request.user
        userproject.project_id = project
        role, res = ProjectRoles.objects.get_or_create(name='Créateur')
        userproject.user_role = role
        
        userproject.save()

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


# ==========================================================
#       PROJECT ROLES API
# ==========================================================


@api_view(['GET'])
def projectrole_list(request):
    roles = ProjectRoles.objects.all()
    serializer = ProjectRolesSerializer(roles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def projectrole_create(request):
    name = request.data['name']
    if name:
        role = ProjectRoles()
        role.name = name
        role.save()

        return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def projectrole_delete(request):
    id = request.data['id']
    if id:
        role = ProjectRoles.objects.get(id=id)
        if role:
            role.delete()
            return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


# ==========================================================
#       USER PROJECT API
# ==========================================================


@api_view(['GET'])
def user_project_list(request, userid):
    user = User.objects.filter(id=userid)[0]
    if user:
        userprojects = user.projects.all()
        projects = set()
        for up in userprojects:
            projects.add(up.project_id)

        return Response(ProjectSerializer(projects, many=True).data, status=status.HTTP_200_OK)
    
    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def project_user_list(request, projectid):
    project = Project.objects.filter(id=projectid)[0]
    if project:
        projectusers = project.users.select_related('user_id', 'user_role').all()
        users = set()
        for user in projectusers:
            users.add(user)
        serializer = UserProjectSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_user_to_project(request):
    userid = request.data['userid']
    projectid = request.data['projectid']
    roleid = request.data['roleid']

    user = User.objects.filter(id=userid)[0]
    project = Project.objects.get(id=projectid)
    role = ProjectRoles.objects.get(id=roleid)

    if user and project and role:
        userproject = UserProject()
        userproject.user_id = user
        userproject.project_id = project
        userproject.user_role = role
        userproject.save()

        return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def delete_user_from_project(request):
    userid = request.data['userid']
    projectid = request.data['projectid']

    userproject = UserProject.objects.filter(user_id=userid, project_id=projectid)
    if userproject:
        userproject.delete()
        return Response({}, status=status.HTTP_200_OK)

    return Response({}, status=status.HTTP_400_BAD_REQUEST)
