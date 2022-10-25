"""test_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from task_app.views import ItemListView, ItemDetailView, SaleCreateView, Login, Logout, SaleListView, HistoryListView
from config.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ItemListView.as_view(), name='items'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('buy-item/', SaleCreateView.as_view(), name='buy-item'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('sale/', SaleListView.as_view(), name='sale'),
    path('item-history/', HistoryListView.as_view(), name='history'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
