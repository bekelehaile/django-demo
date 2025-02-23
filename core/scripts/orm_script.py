from django.contrib.auth.models import User
from django.db.models import Count, Sum, Prefetch
from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint


def handle():
    month_ago = timezone.now() - timezone.timedelta(days=30)
    prefetch = Prefetch(
        "ratings", queryset=Rating.objects.filter(datetime__gte=month_ago)
    )
    restaurants = Restaurant.objects.prefetch_related(prefetch).filter(
        ratings__rating=4
    )
