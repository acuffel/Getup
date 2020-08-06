from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from association.models import Donor, Donation
from account.models import CustomUser, Association, Address
from association.forms import DonorForm


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
                                     first_name='roberto')
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


# Tests Forms

class AssociationFormTestCase(TestCase):
    def test_donor_form(self):
        """
        Creation Nominal Login Form without
        :return: True
        """
        data = {
            'email': 'alfred@wanadoo.fr',
            'first_name': 'Alfred',
            'last_name': 'De la Tour',
            'amount': '10',
        }
        form = DonorForm(data)
        self.assertTrue(form.is_valid())

    def test_donor_form_error(self):
        """
        Creation Erro Login Form with 2 same mails
        :return: True
        """
        Donor.objects.create(email='donor@mail.fr', last_name='carlos',
                                     first_name='roberto')
        data = {
            'email': 'donor@mail.fr',
            'first_name': 'Alfred',
            'last_name': 'De la Tour',
            'amount': '10',
        }
        form = DonorForm(data)
        self.assertEqual(
            form.errors['email'],
            ["Cette email est déjà utilisé"]
        )


# Integration Tests

# Tests Views
class AssociationViewsTestCase(TestCase):
    def setUp(self):
        # Create data sets in every models
        self.address = Address.objects.create(street="23 rue orbe",
                                         state='normandie', zip_code="76000",
                                         city="Rouen", country='France')
        self.association = Association.objects.create(name='MonAsso',
                                                 picture='asso.jpg',
                                                 description='Vive mon Asso',
                                                 category='animaux')
        self.user = User.objects.create_user(username='alex@gmail.com',
                                        email='alex@gmail.com',
                                        password='Password123!',
                                        last_name='carlos',
                                        first_name='roberto')
        self.custom_user = CustomUser.objects.create(user=self.user,
                                                     civility='mr',
                                                     phone='0622222222',
                                                     birth_date='1902-11-02',
                                                     address=self.address,
                                                     association=self.association,
                                                     user_type='AS')
        self.donor = Donor.objects.create(email='donor@mail.fr',
                                          last_name='carlos',
                                          first_name='roberto')
        self.donation = Donation.objects.create(amount='100',
                                                user_id=self.custom_user,
                                                association_id=self.association)

    def test_home_asso(self):
        """
        :return: Status code 200
        """
        asso_id = self.association.id
        response = self.client.get(reverse('association:home_asso',
                                           args=(asso_id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Faire un Don')

    def test_search_city(self):
        """
        :return: Status code 200
        """
        city = self.address.city
        response = self.client.post(reverse('association:search_city'),
                                           {'search_city': city})
        self.assertEqual(response.status_code, 200)

    def test_search_country(self):
        """
        :return: Status code 200
        """
        country = self.address.country
        response = self.client.post(reverse('association:search_country'),
                                           {'search_country': country})
        self.assertEqual(response.status_code, 200)

    def test_search_name(self):
        """
        :return: Status code 200
        """
        name = 'Mon'
        response = self.client.post(reverse('association:search_name'),
                                           {'search_name': name})
        self.assertEqual(response.status_code, 200)

    def test_search_asso(self):
        """
        :return: Status code 200
        """
        response = self.client.get(reverse('association:search_asso'))
        self.assertEqual(response.status_code, 200)

    def test_make_donation(self):
        """
        :return: Status code 200
        """
        data = {
            'email': 'donor@mail.fr',
            'first_name': 'Alfred',
            'last_name': 'De la Tour',
            'amount': '10',
        }
        response = self.client.post(reverse('association:make_donation',
                                    args=(self.association.id,)),
                                            {'context': data})
        self.assertEqual(response.status_code, 200)
