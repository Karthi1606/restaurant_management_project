from django.db import models

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING','pending')
        ('PROCESSING','processing')
        ('COMPLETED','comledeted')
        ('CANCELLED','cancelled')
    ]

    customer = models.ForeingKey(User, On_delete=models.CASECADE, related_name='orders')
    order_item = models.ManyToManyFiled(Menu, related_name='orders')
    total_amount = models.Decimal.Field(max_length=10, decimal_places=2)
    oreder_status = model.CharField(mac_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}