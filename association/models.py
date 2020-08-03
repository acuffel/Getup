from django.db import models
from account.models import CustomUser, Association


# Create a Donor on DB
class Donor(models.Model):
    email = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)


# Create an Event on DB
class Event(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(null=True)
    description = models.TextField(null=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    association_id = models.ForeignKey(Association, on_delete=models.CASCADE)


# Create a Donation on DB
class Donation(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    association_id = models.ForeignKey(Association, on_delete=models.CASCADE,
                                       null=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    donor_id = models.ForeignKey(Donor, null=True, on_delete=models.CASCADE)
