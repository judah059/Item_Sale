from django.contrib import admin

from task_app.models import Item, Employee, PriceHistory


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    pass
