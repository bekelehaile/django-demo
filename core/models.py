from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


def restaurant_name_must_begin_with_a_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Restaurant name must begin with a letter")


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = "In", "Indian"
        CHINESE = "CH", "Chinese"
        ETHIOPIA = "ET", "Ethiopia"
        OTHER = "OT", "Other"

    name = models.CharField(
        max_length=100, validators=[restaurant_name_must_begin_with_a_letter]
    )
    website = models.URLField(default="")
    date_opened = models.DateField()
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    restaurant_type = models.CharField(max_length=3, choices=TypeChoices.choices)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="ratings"
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"Rating: {self.rating}"


class Sale(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.SET_NULL, null=True, related_name="sales"
    )
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()
