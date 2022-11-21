from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(max_length=8),
    price = models.FloatField(max_length=12),
