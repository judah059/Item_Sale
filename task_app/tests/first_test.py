from django.test import TestCase, RequestFactory

from task_app.views import ItemListView


class FirstTest(TestCase):
    fixtures = ['item.json']

    def setUp(self):
        self.factory = RequestFactory()

    def test_base_page(self):
        request = self.factory.get('/')
        response = ItemListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div>banana</div>')
