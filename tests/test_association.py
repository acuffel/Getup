from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from association.models import Donor, Donation
from account.models import CustomUser, Association, Address


# Unit Tests

# Tests Models
class AssociationModelTestCase(TestCase):
    def setUp(self):
        # Create data sets in every models
        address = Address.objects.create(street="23 rue orbe",
                                         state='normandie', zip_code="76000",
                                         city="Rouen", country='France')
        association = Association.objects.create(name='MonAsso',
                                                 picture='asso.jpg',
                                                 description='Vive mon Asso',
                                                 category='animaux')
        user = User.objects.create_user(username='alex@gmail.com',
                                        email='alex@gmail.com',
                                        password='Password123!',
                                        last_name='carlos',
                                        first_name='roberto')
        custom_user = CustomUser.objects.create(user=user, civility='mr',
                                                phone='0622222222',
                                                birth_date='1902-11-02',
                                                address=address,
                                                association=association,
                                                user_type='AS')
        donor = Donor.objects.create(email='donor@mail.fr', last_name='carlos',
                                     first_name='roberto',
                                     phone='061010101010')
        Donation.objects.create(amount='100', user_id=custom_user,
                                            association_id=association)
        Donation.objects.create(amount='20', donor_id=donor,
                                            association_id=association)

    def test_donor(self):
        """
        Get Nominal data set for Address
        :return: street
        """
        donor_test = Donor.objects.get(email='donor@mail.fr')
        self.assertEqual(donor_test.first_name, 'roberto')

    def test_donation(self):
        custom_user = CustomUser.objects.get(
            user=User.objects.get(email='alex@gmail.com'))
        donation1_test = Donation.objects.get(user_id=custom_user)
        donation2_test = Donation.objects.get(
            donor_id=Donor.objects.get(email='donor@mail.fr'))
        self.assertEqual(donation1_test.association_id,
                         Association.objects.get(name='MonAsso'))
        self.assertEqual(donation2_test.association_id,
                         Association.objects.get(name='MonAsso'))
