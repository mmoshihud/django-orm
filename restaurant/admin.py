from django.contrib import admin

from .models import MenuItem, Menu, Order, OrderItem, Restaurant

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
