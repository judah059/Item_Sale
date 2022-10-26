from django.forms import ModelForm

from task_app.models import Sale, Item, MyUser


class AddSaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = [
            'item_count',
            'item',
            'employee',
        ]

    def __init__(self, *args, **kwargs):
        super(AddSaleForm, self).__init__(*args, **kwargs)
        try:
            self.item = kwargs.get('initial')['item']
            self.fields['item'] = self.item
        except KeyError:
            pass
        self.fields['employee'].queryset = MyUser.objects.filter(role='EM')

    def clean(self):
        cleaned_data = super().clean()
        count = cleaned_data.get('item_count')
        item = cleaned_data.get('item')
        if count > item.count:
            self.add_error('item_count', f'Sorry, not enough {item.name}')
        if count <= 0:
            self.add_error('count', f'Please select one or more {item.name}')

