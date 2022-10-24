from annoying.decorators import render_to
from django.db import transaction
from django.views.generic import ListView, FormView, DetailView
from task_app.models import Item, Employee
from task_app.forms import AddSaleForm


class ItemListView(ListView):
    model = Item
    template_name = 'items.html'


class SaleCreateView(FormView):
    form_class = AddSaleForm
    http_method_names = ['post']
    success_url = '/'

    def get_form_kwargs(self):
        kw = super(SaleCreateView, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def form_valid(self, form):
        obj = form.save(commit=False)
        employee_id = self.request.POST.get('employee')
        print(employee_id)
        obj.employee = Employee.objects.get(id=employee_id)
        item_id = self.request.POST.get('item')
        print(item_id)
        obj.item = Item.objects.get(id=item_id)
        obj.item.count = obj.item.count - obj.item_count
        with transaction.atomic():
            obj.item.save()
            obj.save()
        return super().form_valid(form=form)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'itemDetail.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['form'] = AddSaleForm
        context['employees'] = Employee.objects.all()
        return context

    def get_form_kwargs(self):
        kw = super(ItemDetailView, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

