from django.urls import reverse
from django.test import TestCase


# HomePage
class AboutPageTestCase(TestCase):
    # test that home page returns 200
    def test_about_page(self):
        response = self.client.get(reverse('about:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
