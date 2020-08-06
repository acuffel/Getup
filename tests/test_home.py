from django.urls import reverse
from django.test import TestCase


# HomePage
class HomePageTestCase(TestCase):
    # test that home page returns 200
    def test_home_page(self):
        """
        :return: Home page with status code 200
        """
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Je fais un don')
