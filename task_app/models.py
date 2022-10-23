from django.db import models


class Employee(models.Model):
    first_name = models.CharField(
        max_length=100,
    )
    last_name = models.CharField(
        max_length=100,
    )
    city = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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


class Sale(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='sales',
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='employees',
    )
    item_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

