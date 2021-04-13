from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=15)
    zipCode = models.IntegerField()
    phone = models.IntegerField()
