from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ClpmUser

class ClpmUserCreationForm(UserChangeForm):
    class Meta():
        model = ClpmUser
        fields = ('username', 'email')

class ClpmUserChangeForm(UserChangeForm):
    class Meta():
        model = ClpmUser
        fields = ('username', 'email')