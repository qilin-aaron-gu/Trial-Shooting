from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import models

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)
    class Meta:
        model = models.User
        fields = ('username','email', 'password1', 'password2')