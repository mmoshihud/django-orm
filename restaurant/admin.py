from django.contrib import admin

from .models import (
    MenuItem,
    Menu,
    Order,
    OrderItem,
    Review,
    Contact,
    Restaurant,
    RestaurantType,
    MenuItemType,
    Ingredient,
    Dish,
)

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(Contact)
admin.site.register(RestaurantType)
admin.site.register(MenuItemType)
admin.site.register(Ingredient)
admin.site.register(Dish)
