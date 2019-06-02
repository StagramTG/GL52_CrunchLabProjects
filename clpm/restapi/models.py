from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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
    account_id = models.OneToOneField(to=Account, on_delete=models.CASCADE)


"""
Class AccountReload
"""
class AccountReload(models.Model):
    amount     = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    account_id = models.OneToOneField(to=Account, on_delete=models.CASCADE)


"""
Class User
Custom user model that takes differents fields in consideration
for needs of the project.
"""
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    mail       = models.EmailField()
    location   = models.CharField(max_length=256)
    phone      = models.CharField(max_length=15)
    account_id = models.OneToOneField(to=Account, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


"""
Class Project
"""
class Project(models.Model):
    name        = models.CharField(max_length=50)
    description = models.TextField()
    account_id  = models.OneToOneField(to=Account, on_delete=models.CASCADE)
    user_id     = models.OneToOneField(to=User, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


"""
Class Task
"""
class Task(models.Model):
    name       = models.CharField(max_length=128)
    project_id = models.OneToOneField(to=Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField()
    ended_at   = models.DateTimeField()

    def __str__(self):
        return self.name


"""
Class TaskUserAssignement
"""
class TaskUserAssignement(models.Model):
    user_id = models.OneToOneField(to=User, on_delete=models.CASCADE)
    task_id = models.OneToOneField(to=Task, on_delete=models.CASCADE)
