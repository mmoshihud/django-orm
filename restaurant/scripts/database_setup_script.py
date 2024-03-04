from faker import Faker
from ..models import (
    RestaurantType,
    MenuItemType,
    Restaurant,
    Ingredient,
    Dish,
    Menu,
    MenuItem,
    Order,
    OrderItem,
    Review,
    Contact,
)


def run():

    fake = Faker()

    # Add Restaurant Types
    restaurant_types = ["Fast Food", "Fine Dining", "Casual Dining", "Cafe", "Bar"]
    for type_name in restaurant_types:
        RestaurantType.objects.create(name=type_name)

    # Add Menu Item Types
    menu_item_types = ["Appetizer", "Main Course", "Dessert", "Beverage"]
    for type_name in menu_item_types:
        MenuItemType.objects.create(name=type_name)

    # Add Ingredients
    for _ in range(50):
        Ingredient.objects.create(name=fake.word())

    # Add Restaurants
    for _ in range(100):
        restaurant_type = RestaurantType.objects.get(
            name=fake.random_element(restaurant_types)
        )
        Restaurant.objects.create(
            restautant_type=restaurant_type,
            name=fake.company(),
            address=fake.address(),
            phone=fake.phone_number(),
            email=fake.email(),
            website=fake.url(),
            description=fake.text(),
            opening_time=fake.time(),
            closing_time=fake.time(),
        )

    # Add Dishes
    for _ in range(50):
        dish = Dish.objects.create(name=fake.word())
        dish.ingredients.set(Ingredient.objects.order_by("?")[:10])

    # Add Menus
    for restaurant in Restaurant.objects.all():
        for _ in range(1):
            menu = Menu.objects.create(
                restaurant=restaurant,
                name=fake.word(),
                description=fake.text(),
            )
            menu.dish.set(Dish.objects.order_by("?")[:10])

    # Add Menu Items
    for menu in Menu.objects.all():
        for _ in range(5):
            menu_item = MenuItem.objects.create(
                menu=menu,
                menu_item_type=MenuItemType.objects.get(
                    name=fake.random_element(menu_item_types)
                ),
                name=fake.word(),
                description=fake.text(),
                price=fake.pydecimal(left_digits=3, right_digits=2),
            )

    # Add Orders
    for restaurant in Restaurant.objects.all():
        for _ in range(2):  # 100
            order = Order.objects.create(
                restaurant=restaurant,
                name=fake.name(),
                address=fake.address(),
                phone=fake.phone_number(),
                email=fake.email(),
                order_time=fake.date_time_this_month(before_now=True, after_now=False),
                total=fake.pydecimal(left_digits=4, right_digits=2),
            )

    # Add Order Items
    for order in Order.objects.all():
        for _ in range(3):  # 500
            menu_item = MenuItem.objects.order_by("?").first()
            OrderItem.objects.create(
                order=order, menu_item=menu_item, quantity=fake.random_int(1, 5)
            )

    # Add Reviews
    for restaurant in Restaurant.objects.all():
        for _ in range(5):
            Review.objects.create(
                restaurant=restaurant,
                name=fake.name(),
                email=fake.email(),
                rating=fake.random_int(1, 5),
                review=fake.text(),
            )

    # Add Contacts
    for restaurant in Restaurant.objects.all():
        for _ in range(5):
            Contact.objects.create(
                restaurant=restaurant,
                name=fake.name(),
                email=fake.email(),
                message=fake.text(),
            )
