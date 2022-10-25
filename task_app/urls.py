from django.urls import path
from task_app.views import ItemListView, ItemDetailView, SaleCreateView, Login, Logout, SaleListView, HistoryListView


urlpatterns = [
    path('', ItemListView.as_view(), name='items'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('buy-item/', SaleCreateView.as_view(), name='buy-item'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('sale/', SaleListView.as_view(), name='sale'),
    path('item-history/', HistoryListView.as_view(), name='history'),
]
