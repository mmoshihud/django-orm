from collections import Counter
from random import uniform, randint
from restaurant.models import (
    Restaurant,
    Menu,
    MenuItem,
    Order,
    OrderItem,
    Review,
    Contact,
    RestaurantType,
)
from django.db.models import Count, Min, Max, Avg
from django.db import connection


def run():
    # restaurant = Restaurant.objects.values("name", "address").all()[:5]
    # restaurant = Restaurant.objects.values_list("name", flat=True).all()[:5]
    # restaurant = Restaurant.objects.aggregate(total=Count("pk"))
    # menu_item = MenuItem.objects.aggregate(Min("price"), Max("price"), Avg("price"))
    # order_item = OrderItem.objects.aggregate(
    #     Min("quantity"), Max("quantity"), Avg("quantity")
    # )
    restaurants = (
        Restaurant.objects.select_related("restautant_type")
        .prefetch_related(
            "menu_set",
            "order_set",
            "review_set",
            "contact_set",
            "order_set__orderitem_set",
            "menu_set__menuitem_set",
        )
        .annotate(
            min_quantity=Min("order__orderitem__quantity"),
            max_quantity=Max("order__orderitem__quantity"),
            avg_quantity=Avg("order__orderitem__quantity"),
        )
        .first()
    )

    # print(type(menu_item))
    # average_price = order_item.get("quantity__avg")
    # print(average_price)
    # print(type(average_price))
    # print(menu_item)
    # print(order_item)
    # print(uniform(0, 100))
    print(restaurants.min_quantity)

    # print(connection.queries)
