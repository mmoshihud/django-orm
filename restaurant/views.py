from rest_framework.generics import ListAPIView, RetrieveAPIView
from restaurant.models import Menu, Restaurant

from restaurant.serializers import RestaurantDetailSerializer, RestaurantListSerializer
from django.db.models import Prefetch, OuterRef


class RestaurantListView(ListAPIView):
    serializer_class = RestaurantListSerializer
    queryset = Restaurant.objects.select_related("restautant_type").prefetch_related(
        "menu_set", "order_set", "review_set", "contact_set"
    )
    # queryset = Restaurant.objects.filter(pk=1).select_related(
    #     "restautant_type"
    # ) # This is how you can optimize to use select_related is enough if queryset returns only one object


class RestaurantDetailView(RetrieveAPIView):
    serializer_class = RestaurantDetailSerializer

    def get_object(self):
        # here select_related is enough because get object returns only one object
        restaurant = Restaurant.objects.select_related("restautant_type").get(
            pk=self.kwargs["pk"]
        )
        return restaurant
