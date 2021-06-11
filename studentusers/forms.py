from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Student


# to Create User
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'E-mail'}


class StudentUser(ModelForm):
    class Meta:
        model = Student
        fields = ['roll_no', 'div', 'department']
