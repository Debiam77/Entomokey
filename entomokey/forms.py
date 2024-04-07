from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationForm(UserCreationForm):
    username = forms.CharField(label='Nome de Usuario:', help_text='Nome de Usuario')
    first_name = forms.CharField(label='Primeiro Nome (ex: Matheus):')
    email = forms.EmailField(label='Email:')
    password1 = forms.CharField(label='Senha:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme sua Senha:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Nome de Usuario:", max_length=200)
    password = forms.CharField(label='Senha:', widget=forms.PasswordInput)