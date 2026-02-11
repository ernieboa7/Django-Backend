from django.db import models
class Payment(models.Model):
    order = models.OneToOneField('orders.Order', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
