from django.contrib import admin

from task_app.models import Item, Employee


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
