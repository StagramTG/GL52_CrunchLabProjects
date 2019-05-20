from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import ClpmUser
from .forms import ClpmUserCreationForm, ClpmUserChangeForm

# Register your models here.
class ClpmUserAdmin(UserAdmin):
    add_form = ClpmUserCreationForm
    form = ClpmUserChangeForm
    list_display = ['username', 'email',]

admin.site.register(ClpmUser, ClpmUserAdmin)