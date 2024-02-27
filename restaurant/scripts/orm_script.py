from collections import Counter
from random import randint
from restaurant.models import Restaurant
from django.db.models import Count
from django.db import connection


def run():
    # restaurant = Restaurant.objects.values("name", "address").all()[:5]
    # restaurant = Restaurant.objects.values_list("name", flat=True).all()[:5]
    # restaurant = Restaurant.objects.aggregate(total=Count("pk"))
    # print(restaurant)
    # print(connection.queries)
    print("hello world")
