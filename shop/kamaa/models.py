from django.db import models

# Create your models here.
class Product(models.Model):
     name = models.Charfield(max_length=255)
     price = models.DecimalField(max_digits=10, decimal_place=2)
