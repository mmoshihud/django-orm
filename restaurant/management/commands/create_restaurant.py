from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

5
from restaurant.models import (
    Restaurant,
    Menu,
    MenuItem,
    Order,
    OrderItem,
    Review,
    Contact,
)


class Command(BaseCommand):
    help = "Create random data for the database"

    def handle(self, *args, **kwargs):
        for _ in range(10):
            Restaurant.objects.create(
                name=get_random_string(5),
                address=get_random_string(5),
                phone=get_random_string(5),
                email=f"{get_random_string(5)}@gmail.com",
                website=f"http://{get_random_string(5)}.com",
                description=get_random_string(5),
            )

            Menu.objects.create(
                restaurant=Restaurant.objects.order_by("?").first(),
                name=get_random_string(5),
                description=get_random_string(5),
            )

            MenuItem.objects.create(
                menu=Menu.objects.order_by("?").first(),
                name=get_random_string(5),
                description=get_random_string(5),
                price=10.00,
            )

            Order.objects.create(
                restaurant=Restaurant.objects.order_by("?").first(),
                name=get_random_string(5),
                address=get_random_string(5),
                phone=get_random_string(5),
                email=f"{get_random_string(5)}@gmail.com",
                total=10.00,
            )

            OrderItem.objects.create(
                order=Order.objects.order_by("?").first(),
                menu_item=MenuItem.objects.order_by("?").first(),
                quantity=1,
            )

            Review.objects.create(
                restaurant=Restaurant.objects.order_by("?").first(),
                name=get_random_string(5),
                email=f"{get_random_string(5)}@gmail.com",
                rating=1,
                review=get_random_string(5),
            )

            Contact.objects.create(
                restaurant=Restaurant.objects.order_by("?").first(),
                name=get_random_string(5),
                email=f"{get_random_string(5)}@gmail.com",
                message=get_random_string(5),
            )

        self.stdout.write(self.style.SUCCESS("Data populated successfully"))
