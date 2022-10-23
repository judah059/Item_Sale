from annoying.decorators import render_to
from task_app.models import Item


@render_to('items.html')
def item_list(request):
    items = Item.objects.all()
    return {'object_list': items}
