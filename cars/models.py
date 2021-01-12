from django.db import models

from cars.validators import validate_year


class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=35)
    vehicle_shape = models.CharField(max_length=15)
    engine = models.CharField(max_length=15)
    MANUAL = 'Manual Transmission'
    AUT = 'Automatic Transmission'
    TRANSMISSION_CHOICES = (
        (MANUAL, 'Manual'),
        (AUT, 'Automatic'),
    )
    transmission = models.CharField(
        max_length=22,
        choices=TRANSMISSION_CHOICES,
        default=MANUAL,
    )
    horsepower = models.IntegerField()
    torque = models.IntegerField()
    year = models.CharField(
        max_length=4,
        validators=(
            validate_year,
        ),
    )

    cost = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.make} {self.model}'
