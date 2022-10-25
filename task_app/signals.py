import copy

from django.db.models.signals import post_save
from django.dispatch import receiver

from task_app.models import Item, PriceHistory


# maybe we need to use 'pre_save' to check that exactly price was changed
@receiver(post_save, sender=Item)
def create_price_history(sender, instance, created, **kwargs):
    PriceHistory.objects.create(
        item=instance,
        price=instance.price,
    )
