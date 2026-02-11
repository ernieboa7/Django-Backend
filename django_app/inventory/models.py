from django.db import models

class Inventory(models.Model):
    product = models.OneToOneField('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

