# from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model() #반환값은 user settings에다가 AUTH_USER 뭐시기 해놓은거(settings.AUTH_USER_MODEL) 얘는 문자열을 가르키고 우리가 쓰고있는건 class를 가리킴
        fields = ('first_name', 'last_name', 'email',)