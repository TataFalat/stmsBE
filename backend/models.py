import datetime
from django.db import models

class Order(models.Model):
    number = models.CharField(max_length=20)
    customerName = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today)
    
    class Meta:
        ordering = ['number']

class Waypoint(models.Model):
    class Types(models.IntegerChoices):
        DELIVERY = 0, 'Delivery'
        PICKUP = 1, 'Pickup'
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='waypoints')
    location = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=10)
    postalCode = models.CharField(max_length=10) # preferably codelist/dictionary, if available
    city = models.CharField(max_length=100) # preferably codelist/dictionary, if available
    country = models.CharField(max_length=100) # preferably codelist/dictionary, if available 
    type = models.SmallIntegerField(choices=Types, default=Types.DELIVERY)
