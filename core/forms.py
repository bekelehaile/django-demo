from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class RatingForm(forms.Form):
    rating = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
