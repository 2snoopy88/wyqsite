from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class UserProfileForm(ModelForm):
    class Meta:
        model = User

        fields = ('name', 'age', 'sex', 'location', 'company', 'bio')

class UserImgForm(ModelForm):
    class Meta:
        model=User

        fields=('avatar',)