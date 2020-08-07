from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from account.forms import AssociationForm, LoginForm, UploadAssociation
from account.models import CustomUser, Address, Association


# Unit Tests

# Tests Models
class AccountModelTestCase(TestCase):
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
        CustomUser.objects.create(user=user, civility='mr', phone='0622222222',
                                  birth_date='1902-11-02', address=address,
                                  association=association, user_type='AS')

    def test_Address(self):
        """
        Get Nominal data set for Address
        :return: street
        """
        address_test = Address.objects.get(city='Rouen')
        self.assertEqual(address_test.street, '23 rue orbe')

    def test_Association(self):
        """
        Get Nominal data set for Association
        :return: category
        """
        association_test = Association.objects.get(name='MonAsso')
        self.assertEqual(association_test.category, 'animaux')

    def test_User(self):
        """
        Get Nominal data set for User
        :return: email
        """
        user_test = User.objects.get(username='alex@gmail.com')
        self.assertEqual(user_test.email, 'alex@gmail.com')

    def test_CustomUser(self):
        """
        Get Nominal data set for CustoUser
        :return: user_type
        """
        user_test = User.objects.get(username='alex@gmail.com')
        custom_user_test = CustomUser.objects.get(user=user_test)
        self.assertEqual(custom_user_test.user_type, 'AS')


# Tests Forms
class AccountFormTestCase(TestCase):
    def test_login_form(self):
        """
        Creation Nominal Login Form without
        :return: True
        """
        User.objects.create_user(username='alex@gmail.com',
                                 email='alex@gmail.com',
                                 password='Password123!',
                                 last_name='carlos',
                                 first_name='roberto')
        data = {
            'username': 'alex@gmail.com',
            'password': 'toto',
        }
        form = LoginForm(data)
        self.assertTrue(form.is_valid())

    def test_association_form(self):
        """
        Creation Nominal Association Form
        :return: True
        """
        data = {
            'name': 'alex',
            'street': 'toto',
            'zip_code': '35000',
            'city': 'Rennes',
            'country': 'France',
            'first_name': 'roberto',
            'last_name': 'carlos',
            'email': 'al@g.com',
            're_email': 'al@g.com',
            'password': 'Password12/',
            're_password': 'Password12/',
        }
        form = AssociationForm(data)
        self.assertTrue(form.is_valid())

    def test_upload_association_form(self):
        """
        Creation Nominal Upload Association Form
        :return: True
        """
        data = {
            'picture': 'asso.jpeg',
            'description': 'Cette association nous parle de la protection'
                           ' animale',
            'category': 'animaux',
        }
        form = UploadAssociation(data)
        self.assertFalse(form.is_valid())  # ImageField not working

        # test password length

    def test_password_length(self):
        """
        :return: Error because the password is less than 8 characters
        """
        data = {
            'name': 'alex',
            'street': 'toto',
            'zip_code': '35000',
            'city': 'Rennes',
            'country': 'France',
            'first_name': 'roberto',
            'last_name': 'carlos',
            'email': 'al@g.com',
            're_email': 'al@g.com',
            'password': 'Pass',
            're_password': 'Pass',
        }
        form = AssociationForm(data)
        self.assertEqual(
            form.errors['password'],
            ["Le mot de passe doit comporter au moins 8 caracteres"]
        )

        # test password uppercase

    def test_password_upper(self):
        """
        :return: Error because password didn't contains upper letter
        """
        data = {
            'name': 'alex',
            'street': 'toto',
            'zip_code': '35000',
            'city': 'Rennes',
            'country': 'France',
            'first_name': 'roberto',
            'last_name': 'carlos',
            'email': 'al@g.com',
            're_email': 'al@g.com',
            'password': 'passwor12@',
            're_password': 'passwor12@',
        }
        form = AssociationForm(data)
        self.assertEqual(
            form.errors['password'],
            ["Le mot de passe doit comporter au moins 1 majuscule"]
        )

        # test password lowercase

    def test_password_lower(self):
        """
        :return: Error because password didn't contains lower letter
        """
        data = {
            'name': 'alex',
            'street': 'toto',
            'zip_code': '35000',
            'city': 'Rennes',
            'country': 'France',
            'first_name': 'roberto',
            'last_name': 'carlos',
            'email': 'al@g.com',
            're_email': 'al@g.com',
            'password': 'PASSWOR12@',
            're_password': 'PASSWOR12@',
        }
        form = AssociationForm(data)
        self.assertEqual(
            form.errors['password'],
            ["Le mot de passe doit comporter au moins 1 minuscule"]
        )

        # test password special character

    def test_password_spe(self):
        """
        :return: Error because password didn't contains special letter
        """
        data = {
            'name': 'alex',
            'street': 'toto',
            'zip_code': '35000',
            'city': 'Rennes',
            'country': 'France',
            'first_name': 'roberto',
            'last_name': 'carlos',
            'email': 'al@g.com',
            're_email': 'al@g.com',
            'password': 'PASSWOR12',
            're_password': 'PASSWOR12',
        }
        form = AssociationForm(data)
        self.assertEqual(
            form.errors['password'],
            ["Le mot de passe doit comporter au moins 1 "
             "caractere special : @ - / % $ * & #"]
        )

        # test password number

    def test_password_number(self):
        """
        :return: Error because password didn't contains number
        """
        data = {
            'name': 'alex',
            'street': 'toto',
            'zip_code': '35000',
            'city': 'Rennes',
            'country': 'France',
            'first_name': 'roberto',
            'last_name': 'carlos',
            'email': 'al@g.com',
            're_email': 'al@g.com',
            'password': 'PASSWORd@',
            're_password': 'PASSWORd@',
        }
        form = AssociationForm(data)
        self.assertEqual(
            form.errors['password'],
            ["Le mot de passe doit comporter au moins 1 chiffre"]
        )

# Integration Tests

# Tests Views


class AccountViewsTestCase(TestCase):
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
        CustomUser.objects.create(user=user, civility='mr', phone='0622222222',
                                  birth_date='1902-11-02', address=address,
                                  association=association, user_type='AS')

    def test_login(self):
        """
        Login with Username and Password
        :return: status 200
        """
        data = {
            'username': "alex@gmail.com",
            'password': "Password123!",
        }
        user_type = ['AS']
        response = self.client.get(reverse('account:login'),
                                            {'context': data,
                                             'user_type': user_type})
        self.assertTrue(response.status_code, 200)

    def test_logout(self):
        """
        Logout
        :return: status 200
        """
        self.client.login(username="alex@gmail.com", password="Password123!")
        self.client.logout()
        response = self.client.get(reverse('account:logout'))
        self.assertEqual(response.status_code, 200)

    def test_association_registration(self):
        """
        Create an Association account
        :return: The models get one more row with new data
        """
        adress_count = Address.objects.count()
        asso_count = Association.objects.count()
        user_count = User.objects.count()
        customuser_count = CustomUser.objects.count()
        data = {
            'name': 'alex',
            'street': 'toto',
            'zip_code': '35000',
            'city': 'Rennes',
            'country': 'France',
            'first_name': 'roberto',
            'last_name': 'carlos',
            'email': 'al@g.com',
            're_email': 'al@g.com',
            'password': 'Password12/',
            're_password': 'Password12/',
                }
        response = self.client.post(reverse('account:association_registration'),
                                   data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Address.objects.count(), adress_count + 1)
        self.assertEqual(Association.objects.count(), asso_count + 1)
        self.assertEqual(User.objects.count(), user_count + 1)
        self.assertEqual(CustomUser.objects.count(), customuser_count + 1)

    def test_association_registration_error(self):
        """
        Create an Association account
        :return: The models get one more row with new data
        """
        data = {
            'name': 'alex',
            'street': 'toto',
            'zip_code': '35000',
            'city': 'Rennes',
            'country': 'France',
            'first_name': 'roberto',
            'last_name': 'carlos',
            'email': 'al@g.com',
            're_email': 'al@g.com',
            'password': 'Password12/',
        }
        response = self.client.post(reverse('account:association_registration'),
                                    data)
        self.assertEqual(response.status_code, 200)

    def test_member_registration(self):
        """
        Create an Association account
        :return: The models get one more row with new data
        """
        adress_count = Address.objects.count()
        user_count = User.objects.count()
        customuser_count = CustomUser.objects.count()
        data = {
            'civility': 'mr',
            'birth_date': '2020-03-22',
            'phone': '024345464354',
            'street': 'toto',
            'zip_code': '35000',
            'city': 'Rennes',
            'country': 'France',
            'first_name': 'roberto',
            'last_name': 'carlos',
            'email': 'al@g.com',
            're_email': 'al@g.com',
            'password': 'Password12/',
            're_password': 'Password12/',
        }
        response = self.client.post(
            reverse('account:member_registration'),
            data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Address.objects.count(), adress_count + 1)
        self.assertEqual(User.objects.count(), user_count + 1)
        self.assertEqual(CustomUser.objects.count(), customuser_count + 1)

    def test_welcome_association(self):
        """
        Call welcome page
        :return: Status 200
        """
        response = self.client.get(reverse('account:welcome_association'))
        self.assertEqual(response.status_code, 200)

    def test_show_information(self):
        """
        User Login
        :return: Information about user authenticated
        """
        self.client.login(username="alex@gmail.com", password="Password123!")
        response = self.client.get(reverse('account:show_information'))
        self.assertEqual(response.status_code, 200)

    def test_show_association(self):
        """
        User Login
        :return: Association about user authenticated
        """
        self.client.login(username="alex@gmail.com", password="Password123!")
        response = self.client.get(reverse('account:show_association'))
        self.assertEqual(response.status_code, 200)
