from rest_framework import serializers
from . import models

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ('id', 'balance', 'name')


class AccountTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountTransaction
        fields = ('id', 'amount', 'created_at', 'account_id')


class AccountReloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountReload
        fields = ('id', 'amount', 'created_at', 'account_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'location', 
            'phone', 'account_id', 'is_admin'
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = (
            'id', 'name', 'description', 'account_id', 'user_id', 
            'created_at'
        )


class ProjectRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectRoles
        fields = ('id', 'name')


class UserProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProject
        fields = ('id', 'user_id', 'project_id', 'user_role')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = (
            'id', 'name', 'project_id', 'created_at', 'started_at', 
            'ended_at'
        )


class TaskUserAssignementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskUserAssignement
        fields = ('id', 'user_id', 'task_id')