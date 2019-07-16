from django.db import models
from django.db.models.functions import Length
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator


class ValidDataManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(len_fname=Length('first_name'), len_lname=Length('last_name')).filter(
            age__gte=18,
            age__lte=99,
            experience__gte=0,
            experience__lte=240,
            len_fname__gte=2,
            len_fname__lte=32,
            len_lname__gte=4,
            len_lname__lte=64
        )


class MyModel(models.Model):
    # age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)], null=False)
    # experience = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(240)], null=False)
    # first_name = models.CharField(validators=[MinLengthValidator(2)], max_length=32, null=False)
    # last_name = models.CharField(validators=[MinLengthValidator(4)], max_length=64, null=False)
    objects = models.Manager()
    valid_objects = ValidDataManager()
    age = models.PositiveIntegerField(null=True)
    experience = models.PositiveIntegerField(null=True)
    first_name = models.CharField(null=True, max_length=100)
    last_name = models.CharField(null=True, max_length=100)
