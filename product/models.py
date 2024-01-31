from django.db import models

class Product(models.Model):
    WATER_TYPES = [
        ('SS', 'Salt Spring'),
        ('O2', 'O2 Water'),
        ('MDS', 'Regular Water'),
        ('OZ', 'Ozone Water'),
    ]

    SIZE_CHOICES = [
        (5, 'Large (5 Gallon)'),
        (3, 'Small (3 Gallon)'),
    ]

    water_type = models.CharField("Water Type" , max_length = 3 , choices = WATER_TYPES)
    bottle_size = models.IntegerField("Bottle Size", choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits = 5 , decimal_places = 2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['water_type', 'bottle_size'], name='water_type_size')
        ]




    