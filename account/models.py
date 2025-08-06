from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Menu(models.Model):
    name = models.Charfield(maxlenth=100)
    description = model.TextField(blank=True)
    price = models.DecimalField(max_digit=8, decimal_places=2) 

    def __str__(self):
        return self.name