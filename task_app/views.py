from annoying.decorators import render_to
from django.views.generic import ListView
from task_app.models import Item


class ItemListView(ListView):
    model = Item
    template_name = 'items.html'
