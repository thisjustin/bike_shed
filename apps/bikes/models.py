import os
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

img_path = 'apps/bikes/static/bikes/img/'


class Brand(models.Model):
    """'blank & null attributes enables by default"""
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to=img_path)

    def get_logo(self):
        return os.path.basename(self.logo.name)

    def __str__(self):
        return self.__class__.__name__


class Bike(models.Model):
    TYPE_CHOICES = (
        ("MN", "Mountain"),
        ("HB", "Hybrid"),
        ("RD", "Road"),
    )

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='bike')
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, validators=[RegexValidator(r'^(MN|HB|RD)$')])

    model = models.CharField(max_length=255)
    headline = models.CharField(max_length=100)
    image = models.ImageField(upload_to=img_path)
    description = models.TextField(max_length=500)

    size = models.IntegerField(validators=[MinValueValidator(12), MaxValueValidator(30)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def get_image(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.__class__.__name__
