from django.urls import resolve
from django.test import TestCase
from users.views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_rul_resolves_to_home_page_view(self):
        found = resolve('/users/')
        self.assertEqual(found.func, home_page)
