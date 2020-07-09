from django.test import TestCase
from django.contrib.auth.models import User

from account.forms import AssociationForm
from account.models import CustomUser, Address, Association


class AccountTestCase(TestCase):
    def setUp(self):
        address = Address.objects.create(street="23 rue orbe", state='normandie',
                               zip_code="76000", city="Rouen", country='France')
        association = Association.objects.create(name="WWF")
        user = User.objects.create(email='alex@gmail.com', password="Motdepasse147/")
        CustomUser.objects.create(user=user, civility='MR',
                                  phone="0033612345465", birth_date='2023-03-22',
                                  address_id=address, association_id=association,
                                  type_user_choices="ME")

    def test_customUser_creation(self):
        custom_user = CustomUser.objects.get(pk=1)
        self.assertEqual(custom_user.user.email, 'alex@gmail.com')

    """
    def test_association_form(self):
        data = {
        'name': 'Save the world',
        'street': '34 rue orbe',
        'post_code': '76000',
        'city': 'Rouen',
        'country': 'France',
        'first_name': 'Alexandre',
        'last_name': 'CUFFEL',
        'birth_date': '13-03-1987',
        'email': 'alex@gmail.com',
        'password': 'Motdepasse147/',
        }
        form = AssociationForm(data)
        self.assertTrue(form.is_valid())
        """

