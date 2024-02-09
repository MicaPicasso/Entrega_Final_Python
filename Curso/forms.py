from django import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
class ProductosForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"


class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = models.Proveedor
        fields = "__all__"


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model= User
        fields= ["username", "password"]
        widgets= {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields= ["username", "password1", "password2"]
        widgets= {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
