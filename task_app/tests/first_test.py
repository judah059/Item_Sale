from django.test import TestCase, RequestFactory

from task_app.views import ItemListView, SaleCreateView
from task_app.models import Sale


class FirstTest(TestCase):
    fixtures = ['models.json']

    def setUp(self):
        self.factory = RequestFactory()

    def test_base_page(self):
        request = self.factory.get('buy-item/')
        response = ItemListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_add_sale(self):
        request = self.factory.post('buy-item/', {
            'item': 1,
            'employee': 1,
            'item_count': 2,
        }, follow=True)
        response = SaleCreateView.as_view()(request)
        sale_item = Sale.objects.get(id=1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(sale_item.item_count, 2)
