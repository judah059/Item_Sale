from django.contrib import admin

from task_app.models import Item, MyUser, PriceHistory, Sale


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass


@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    search_fields = ['item__name']
    list_display = ('item', 'price', 'created_at')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass
