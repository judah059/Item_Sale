from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.views.generic import ListView, DetailView, CreateView
from task_app.models import Item, MyUser, Sale, PriceHistory
from task_app.forms import AddSaleForm


class ItemListView(ListView):
    model = Item
    template_name = 'items.html'


class SaleCreateView(LoginRequiredMixin, CreateView):
    form_class = AddSaleForm
    success_url = '/'
    login_url = '/login/'

    def form_valid(self, form):
        obj = form.save(commit=False)
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
        context['form'] = AddSaleForm(initial={'item': self.get_object()})
        return context


class Login(LoginView):
    template_name = 'login.html'


class Logout(LogoutView):
    next_page = '/'
    login_url = '/login/'


class SaleListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Sale
    template_name = 'Sale.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super(SaleListView, self).get_queryset()
        return qs.all().select_related('item', 'employee')


class HistoryListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = PriceHistory
    template_name = 'history.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        item_id = self.request.GET.get('pk')
        return qs.filter(item__id=item_id)

    def get_context_data(self, **kwargs):
        context = super(HistoryListView, self).get_context_data(**kwargs)
        item_id = self.request.GET.get('pk')
        context['item'] = Item.objects.get(id=item_id)
        return context
