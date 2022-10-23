from django.contrib import admin

from task_app.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
