from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint


def run():
    restaurant = Restaurant.objects.first()
    user = User.objects.first()
    pprint(
        Rating.objects.get_or_create(
            user=user,
            restaurant=restaurant,
            rating=4.0,
        )
    )
