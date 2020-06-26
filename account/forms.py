from django.forms import ModelForm, TextInput, EmailInput, \
    PasswordInput, ValidationError
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django import forms
import re

from .models import Member


# Manage Error in account page
class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(
            ['<p class="small error">%s</p>' % e for e in self])


# Create LoginForm
class LoginForm(ModelForm):
    email = forms.CharField(initial='Email', label='')
    password = forms.CharField(initial='Password', label='')

    class Meta:
        model = Member
        fields = ['email', 'password']


# Create CreationForm
class MemberForm(ModelForm):
    civility = forms.CharField(label='Civilité')
    first_name = forms.CharField(label='Prenom')
    last_name = forms.CharField(label='Nom')
    birth_date = forms.DateField(label='Date de naissance')
    country = forms.CharField(label='Pays')
    email1 = forms.CharField(label='Adresse email')
    email2 = forms.CharField(label='Confirmez votre adresse email')
    password1 = forms.CharField(label='Mot de passe')
    password2 = forms.CharField(label='Confirmez votre mot de passe')

    class Meta:
        model = Member
        fields = ['civility', 'first_name', 'last_name', 'birth_date',
                  'country', 'email1', 'email2', 'password1', 'password2',
                  'address']
        widget = {
            'email1': EmailInput(attrs={'class': 'form-control'}),
            'email2': EmailInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
        }

    # Check if email is not used
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Cette email est déjà utilisé")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        special_characters = ['@', '-', '/', '%', '$', '*', '&', '#']
        if len(password) < 8:
            raise ValidationError("Le mot de passe doit comporter"
                                            " au moins 8 caracteres")
        if not any(c in special_characters for c in password):
            raise ValidationError(
                "Le mot de passe doit comporter au moins 1 "
                "caractere special : @ - / % $ * & #")
        if re.search('[a-z]', password) is None:
            raise ValidationError(
                "Le mot de passe doit comporter au moins 1 minuscule")
        if re.search('[A-Z]', password) is None:
            raise ValidationError(
                "Le mot de passe doit comporter au moins 1 majuscule")
        if re.search('[0-9]', password) is None:
            raise ValidationError(
                "Le mot de passe doit comporter au moins 1 chiffre")
        return password
