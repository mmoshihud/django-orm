from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from random import randint, randbytes

from restaurant.models import (
    Restaurant,
    Menu,
    MenuItem,
    Order,
    OrderItem,
    RestaurantType,
    Review,
    Contact,
)


class Command(BaseCommand):
    help = "Create random data for the database"

    def handle(self, *args, **kwargs):
        for _ in range(100):
            restaurant_type = RestaurantType.objects.create(
                name=get_random_string(5),
            )

            restaurant = Restaurant.objects.create(
                restautant_type=restaurant_type,
                name=get_random_string(5),
                address=get_random_string(5),
                phone="+8801" + randint(100000000, 999999999).__str__(),
                email=f"{get_random_string(5)}@gmail.com",
                website=f"http://{get_random_string(5)}.com",
                description=get_random_string(5),
            )

            Menu.objects.create(
                restaurant=restaurant,
                name=get_random_string(5),
                description=get_random_string(5),
            )

            MenuItem.objects.create(
                menu=Menu.objects.filter(restaurant=restaurant).first(),
                name=get_random_string(5),
                description=get_random_string(5),
                price=randint(1, 100000),
            )

            order = Order.objects.create(
                restaurant=restaurant,
                name=get_random_string(5),
                address=get_random_string(5),
                phone=get_random_string(5),
                email=f"{get_random_string(5)}@gmail.com",
                total=randint(1, 100),
            )

            OrderItem.objects.create(
                order=order,
                menu_item=MenuItem.objects.filter(menu__restaurant=restaurant).first(),
                quantity=randint(1, 1000),
            )

            Review.objects.create(
                restaurant=restaurant,
                name=get_random_string(5),
                email=f"{get_random_string(5)}@gmail.com",
                rating=randint(1, 5),
                review=get_random_string(5),
            )

            Contact.objects.create(
                restaurant=restaurant,
                name=get_random_string(5),
                email=f"{get_random_string(5)}@gmail.com",
                message=get_random_string(5),
            )

        self.stdout.write(self.style.SUCCESS("Data populated successfully"))
