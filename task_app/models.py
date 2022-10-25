from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('RE', 'Regular'),
        ('EM', 'Employee')
    ]
    role = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default='RE',
    )
    city = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )


class Item(models.Model):
    name = models.CharField(
        max_length=120,
    )
    description = models.CharField(
        max_length=300,
    )
    count = models.IntegerField()
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    def __str__(self):
        return self.name


class Sale(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='sales',
    )
    employee = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='sales',
    )
    item_count = models.IntegerField()
    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.item.price * self.item_count
        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.item} by {self.employee}'


class PriceHistory(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='history',
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item} history'
