from django.db import models
from django.contrib.auth.models import AbstractUser

from enum import Enum

class ClpmRoles(Enum):
    ADMIN = "Admin"
    USER  = "User"

# Create your models here.
class ClpmUser(AbstractUser):
    # Add role field to user
    role = models.CharField(
        max_length = 5,
        choices = [(tag, tag.value) for tag in ClpmRoles],
        default = ClpmRoles.USER
    )
    