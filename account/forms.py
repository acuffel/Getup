from django.forms import ModelForm, EmailInput, \
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
        return '<div style="color: white;" class="errorlist">%s</div>' % ''.join(
            ['<p class="small error">%s</p>' % e for e in self])


# Create LoginForm
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'size': 20, 'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.TextInput(
        attrs={'size': 20, 'placeholder': 'Mot de passe'}), label='')

    class Meta:
        model = User
        fields = ['username', 'password']
        widget = {
            'username': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
        }


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
        re_email = self.cleaned_data.get('re_email')
        if email != re_email:
            raise ValidationError("Les emails ne correspondent pas")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Cette email est déjà utilisé")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise ValidationError("Les mots de passe ne correspondent pas")
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
    name = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    street = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    zip_code = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'size': 15, 'placeholder': 'Code Postal'}))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={'size': 15, 'placeholder': 'Ville'}))
    country = forms.CharField(
        widget=forms.TextInput(attrs={'size': 15, 'placeholder': 'Pays'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'size': 25, 'placeholder': 'Prénom'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'size': 25, 'placeholder': 'Nom'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'size': 25, 'placeholder': 'Email'}))
    re_email = forms.CharField(
        widget=forms.TextInput(
            attrs={'size': 25, 'placeholder': 'Confirmez votre email'}))
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={'size': 25, 'placeholder': 'Mot de passe'}))
    re_password = forms.CharField(
        widget=forms.TextInput(
            attrs={'size': 25, 'placeholder': 'Confirmez votre mot de passe'}))

    class Meta:
        model = CustomUser
        fields = ['name', 'street', 'zip_code', 'city',
                  'country', 'first_name', 'last_name', 'email',
                  're_email', 'password', 're_password']
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

    def clean_re_email(self):
        re_email = self.cleaned_data.get('re_email')
        email = self.clean_email()
        print(re_email)
        print(email)
        if email != re_email:
            raise ValidationError("Les Emails ne correspondent pas")
        return re_email

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

    def clean_re_password(self):
        re_password = self.cleaned_data.get('re_password')
        password = self.clean_password()
        if password != re_password:
            raise ValidationError("Les Mots de passe ne correspondent pas")
        return re_password
