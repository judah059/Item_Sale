from django.forms import ModelForm

from task_app.models import Sale, Item


class AddSaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = [
            'item_count',
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddSaleForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        count = cleaned_data.get('item_count')
        item_id = self.request.POST.get('item')
        item = Item.objects.get(id=item_id)
        if count > item.count:
            self.add_error('item_count', f'Sorry, not enough {item.name}')
        if count <= 0:
            self.add_error('count', f'Please select one or more {item.name}')
