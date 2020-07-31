from django.forms import ModelForm, EmailInput, ValidationError
from django import forms

from .models import Donor


# Create LoginForm
class DonorForm(ModelForm):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'size': 20, 'placeholder': 'Email'}), label='')
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'size': 20, 'placeholder': 'Prenom'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'size': 20, 'placeholder': 'Nom'}), label='')
    amount = forms.IntegerField(widget=forms.TextInput(
        attrs={'size': 20, 'placeholder': '--,--'}), label='')

    class Meta:
        model = Donor
        fields = ['email', 'first_name', 'last_name', 'amount']
        widget = {
            'username': EmailInput(attrs={'class': 'form-control'}),
        }

    # Check if email is not used
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Donor.objects.filter(email=email).exists():
            raise ValidationError("Cette email est déjà utilisé")
        return email
