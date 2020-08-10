from django.db import models
from django.contrib.auth.models import User


# Create an Address on DB
class Address(models.Model):
    street = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=100, null=True)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


# Create an Association on DB
class Association(models.Model):
    name = models.CharField(max_length=100, unique=True)
    picture = models.ImageField(upload_to='images/',
                                default='images/no_image.png')
    description = models.TextField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, null=True)
    mission = models.TextField(null=True)
    action = models.TextField(null=True)
    difficulty = models.TextField(null=True)
    need = models.TextField(null=True)

    def __str__(self):
        return self.name


# Create a Custom User based on User library Django
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    civility = models.CharField(max_length=3, null=True)
    phone = models.CharField(max_length=15, null=True)
    birth_date = models.DateField(null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    association = models.OneToOneField(Association, on_delete=models.CASCADE,
                                       null=True)
    user_type = models.CharField(max_length=2)
