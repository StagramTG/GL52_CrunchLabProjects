from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

"""
Class Account
Store the money balance between reload and transaction
"""
class Account(models.Model):
    balance = models.FloatField()
    name    = models.CharField(max_length=50)

    def __str__(self):
        return self.name


"""
Class AccountTransaction
"""
class AccountTransaction(models.Model):
    amount     = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    account_id = models.ForeignKey(to=Account, on_delete=models.CASCADE)


"""
Class AccountReload
"""
class AccountReload(models.Model):
    amount     = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    account_id = models.ForeignKey(to=Account, on_delete=models.CASCADE)

"""
Class User
Custom user model that takes differents fields in consideration
for needs of the project.
"""
class User(AbstractUser):
    email      = models.EmailField(unique=True)
    location   = models.CharField(max_length=255, blank=True)
    phone      = models.CharField(max_length=15, blank=True)
    account_id = models.ForeignKey(to=Account, on_delete=models.CASCADE, blank=True, null=True)
    is_admin   = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    class Meta:
        abstract = False

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


"""
Class Project
"""
class Project(models.Model):
    name        = models.CharField(max_length=50)
    description = models.TextField()
    account_id  = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    user_id     = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


"""
Class ProjectRoles
"""
class ProjectRoles(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


"""
Class UserProject
"""
class UserProject(models.Model):
    user_id    = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='projects')
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='users')
    user_role  = models.ForeignKey(to=ProjectRoles, on_delete=models.CASCADE, blank=True, null=True)


"""
Class Task
"""
class Task(models.Model):
    name       = models.CharField(max_length=128)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField()
    ended_at   = models.DateTimeField()

    def __str__(self):
        return self.name


"""
Class TaskUserAssignement
"""
class TaskUserAssignement(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    task_id = models.ForeignKey(to=Task, on_delete=models.CASCADE)


"""
Class ShopProducts
"""
class ShopProduct(models.Model):
    name        = models.CharField(max_length=128)
    price       = models.FloatField()
    description = models.TextField()
