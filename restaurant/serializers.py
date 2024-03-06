from rest_framework import serializers

from restaurant.models import (
    Contact,
    Dish,
    Ingredient,
    Menu,
    MenuItem,
    MenuItemType,
    Order,
    OrderItem,
    Restaurant,
    RestaurantType,
    Review,
)


class RetaurantTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantType
        fields = "__all__"


class RestaurantSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Dish
        fields = "__all__"


class menuItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemType
        fields = "__all__"


class RestaurantMenuItemsSerializer(serializers.ModelSerializer):
    menu_item_type = menuItemTypeSerializer()

    class Meta:
        model = MenuItem
        fields = "__all__"


class RestaurantMenuSerializer(serializers.ModelSerializer):
    menu_items = RestaurantMenuItemsSerializer(source="menuitem_set", many=True)
    dish = DishSerializer(many=True)

    class Meta:
        model = Menu
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = RestaurantMenuItemsSerializer()

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(source="orderitem_set", many=True)

    class Meta:
        model = Order
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class GoodReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    restaurant = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()
    rating = serializers.IntegerField()
    review = serializers.CharField()


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class RestaurantListSerializer(serializers.ModelSerializer):
    total_reviews = serializers.IntegerField()
    good_reviews_count = serializers.IntegerField()
    bad_reviews_count = serializers.IntegerField()
    average_rating = serializers.FloatField()
    menu = RestaurantMenuSerializer(source="menu_set", many=True)
    restautant_type = RetaurantTypeSerializer()
    order = OrderSerializer(source="order_set", many=True)
    contact = ContactSerializer(source="contact_set", many=True)
    good_reviews = GoodReviewSerializer(many=True)

    """If you want to include different field for retaurant type, you can do it like this: 
    any_name = serializers.RetaurantTypeSerializer(source="restautant_type")"""

    class Meta:
        model = Restaurant
        fields = "__all__"

    # review = ReviewSerializer(source="review_set", many=True)
    # good_reviews = GoodReviewSerializer(many=True)

    # def get_good_reviews(self, obj):
    #     # Assuming that "good_reviews" is an attribute containing reviews with rating__gte=5
    #     print(obj.good_reviews)
    #     return TestReviewSerializer(obj.good_reviews, many=True).data

    # def to_representation(self, instance):
    #     # Call the parent class's to_representation method to get the default representation
    #     representation = super().to_representation(instance)

    #     # Add the representation of the 'good_reviews' field
    #     representation["good_reviews"] = TestReviewSerializer(
    #         instance.good_reviews, many=True
    #     ).data

    #     return representation


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
