from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
class CursoFormulario(forms.Form):
    curso= forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    email = forms.EmailField(required=False)
    profesion = forms.CharField()

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text='',
        widget=forms.HiddenInput(),required=False
    )

    class Meta:
        model:User
        fields=['email','first_name','last_name']


