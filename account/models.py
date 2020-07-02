from django.db import models
from django.contrib.auth.models import User


# Create an Address on DB
class Address(models.Model):
    street = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


# Create an Association on DB
class Association(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(null=True)
    description = models.TextField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)


# Create a Custom User based on User library Django
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    civility = models.CharField(max_length=3, null=True)
    phone = models.CharField(max_length=15, null=True)
    birth_date = models.DateField(null=True)
    address_id = models.OneToOneField(Address, on_delete=models.CASCADE)
    association_id = models.OneToOneField(Association, on_delete=models.CASCADE)
    MEMBER = 'ME'
    MANAGER = 'MA'
    TYPE_USER_CHOICES = (
        (MEMBER, 'Member'),
        (MANAGER, 'Manager'),
    )
    type_user_choices = models.CharField(
        max_length=2,
        choices=TYPE_USER_CHOICES,
    )

