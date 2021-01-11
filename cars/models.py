from django.core.validators import MaxLengthValidator
from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=35)
    vehicle_shape = models.CharField(max_length=15)
    engine = models.CharField(max_length=15)
    horsepower = models.IntegerField()
    torque = models.IntegerField()
    year = models.IntegerField(MaxLengthValidator(4))
    cost = models.IntegerField()
