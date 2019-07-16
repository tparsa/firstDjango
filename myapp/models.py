from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

class MyModel(models.Model):
    # age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)], null=False)
    # experience = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(240)], null=False)
    # first_name = models.CharField(validators=[MinLengthValidator(2)], max_length=32, null=False)
    # last_name = models.CharField(validators=[MinLengthValidator(4)], max_length=64, null=False)

    age = models.PositiveIntegerField(null=True)
    experience = models.PositiveIntegerField(null=True)
    first_name = models.CharField(null=True, max_length=100)
    last_name = models.CharField(null=True, max_length=100)
