from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from task_app.views import ItemListView, SaleCreateView, SaleListView
from task_app.models import Sale, Item, PriceHistory, MyUser


class FirstTest(TestCase):
    fixtures = ['models.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.user = MyUser.objects.create_user(username='john', password='1')

    def test_base_page(self):
        request = self.factory.get('/')
        response = ItemListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_add_sale(self):
        request = self.factory.post('buy-item/', {
            'item': 1,
            'employee': 2,
            'item_count': 2,
        }, follow=True)
        request.user = self.user
        response = SaleCreateView.as_view()(request)
        sale_item = Sale.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(sale_item.item_count, 2)

    def test_not_authorized_user(self):
        request = self.factory.get('sale/')
        request.user = AnonymousUser()
        response = SaleListView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=/sale')

    def test_authorized_user(self):
        request = self.factory.get('sale/')
        request.user = self.user
        response = SaleListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_price(self):
        item = Item.objects.first()
        item.price = 500
        item.save()
        price_history = PriceHistory.objects.last()
        self.assertEqual(price_history.price, 500)

    def test_sale_total_price(self):
        item = Item.objects.first()
        Sale.objects.create(
            item=item,
            employee=MyUser.objects.filter(role='EM').first(),
            item_count=2,
        )
        item.price = 1000
        item.save()
        sale = Sale.objects.get(item=item, item_count=2)
        self.assertEqual(sale.total_price, 200)
