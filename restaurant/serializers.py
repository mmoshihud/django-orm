from rest_framework import serializers

from restaurant.models import Contact, Menu, Order, Restaurant, RestaurantType, Review


class RetaurantTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantType
        fields = "__all__"


class RestaurantSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class RestaurantListSerializer(serializers.ModelSerializer):
    menu = RestaurantMenuSerializer(source="menu_set", many=True)
    restautant_type = RetaurantTypeSerializer()
    order = OrderSerializer(source="order_set", many=True)
    review = ReviewSerializer(source="review_set", many=True)
    contact = ContactSerializer(source="contact_set", many=True)

    """If you want to include different field for retaurant type, you can do it like this: 
    any_name = serializers.RetaurantTypeSerializer(source="restautant_type")"""

    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantDetailSerializer(serializers.ModelSerializer):
    menu = RestaurantMenuSerializer(source="menu_set", many=True)
    restautant_type = RetaurantTypeSerializer()
    order = OrderSerializer(source="order_set", many=True)
    review = ReviewSerializer(source="review_set", many=True)
    contact = ContactSerializer(source="contact_set", many=True)

    class Meta:
        model = Restaurant
        fields = "__all__"
        # depth = 1
        # """depth = 1 will include all the fields of the foreign key model"""
