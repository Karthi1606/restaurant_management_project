from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_length=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING','pending')
        ('PROCESSING','processing')
        ('COMPLETED','comledeted')
        ('CANCELLED','cancelled')
    ]

    customer = models.ForeingKey(User, on_delete=models.CASECADE, related_name='orders')
    order_item = models.ManyToManyFiled(Menu, through='OrdersItem')
    total_amount = models.Decimal.Field(max_length=10, decimal_places=2)
    oreder_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id} by {self.customer.username}'

class OrdersItem(models.Model):
    order = models.ForeingKey(Order, on_delete=models.CASECADE)
    menu = models.ForeingKey(Menu, on_delete=models.CASECADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.menu.name}'
