from django.forms import ModelForm, Textarea, EmailInput, \
    PasswordInput, ValidationError
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django import forms
import re

from .models import CustomUser


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
        model = CustomUser
        fields = ['email', 'password']


# Create MemberForm
class MemberForm(ModelForm):
    civility = forms.CharField(label='Civilité')
    first_name = forms.CharField(label='Prenom')
    last_name = forms.CharField(label='Nom')
    birth_date = forms.DateField(label='Date de naissance')
    email = forms.CharField(label='Adresse email')
    re_email = forms.CharField(label='Validez votre adresse email')
    password = forms.CharField(label='Mot de passe')
    re_password = forms.CharField(label='Validez votre mot de passe')

    class Meta:
        model = CustomUser
        fields = ['civility', 'first_name', 'last_name', 'birth_date',
                  'email', 're_email', 'password', 're_password']
        widget = {
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
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


# Create AssociationForm
class AssociationForm(ModelForm):
    name = forms.CharField(label='name')
    address = forms.CharField(label='')
    post_code = forms.DateField(label='', initial='Code Postal')
    city = forms.DateField(label='', initial='Ville')
    country = forms.DateField(label='', initial='Pays')
    first_name = forms.CharField(label='', initial='Prénom')
    last_name = forms.CharField(label='', initial='Nom')
    email = forms.CharField(label='', initial='Email')
    re_email = forms.CharField(label='', initial='Confirmez email')
    password = forms.CharField(label='', initial='Mot de passe')
    re_password = forms.CharField(label='', initial='Confirmez mot de passe')

    class Meta:
        model = CustomUser
        fields = ['name', 'address', 'post_code', 'city',
                  'country', 'first_name', 'last_name', 'email',
                  're_email', 'password', 're_password']
        widget = {
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    # Check if email is not used
    def clean_a_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Cette email est déjà utilisé")
        return email

    def clean_a_password(self):
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
