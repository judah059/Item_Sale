from django.test import TestCase


class FirstTest(TestCase):
    def test_base_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
