from django.db import models


# Create an Address on DB
class Address(models.Model):
    street = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


# Create a Member on DB
class Member(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    civility = models.CharField(max_length=3)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True)
    birth_date = models.DateField()
    address_id = models.OneToOneField(Address, on_delete=models.CASCADE)


# Create a Manager on DB
class Manager(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    civility = models.CharField(max_length=3)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True)


# Create an Association on DB
class Association(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(null=True)
    description = models.TextField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    manager_id = models.OneToOneField(Manager, on_delete=models.CASCADE)
    address_id = models.OneToOneField(Address, on_delete=models.CASCADE)


# Create a Donor on DB
class Donor(models.Model):
    email = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True)


# Create an Event on DB
class Event(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(null=True)
    description = models.TextField(null=True)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    association_id = models.ForeignKey(Association, on_delete=models.CASCADE,
                                       null=True)


# Create a Donation on DB
class Donation(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    association_id = models.ForeignKey(Association, on_delete=models.CASCADE,
                                       null=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    donor_id = models.OneToOneField(Donor, null=True, on_delete=models.CASCADE)




