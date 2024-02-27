from django.shortcuts import render

from rest_framework.generics import ListAPIView
from restaurant.models import Restaurant

from restaurant.serializers import RestaurantListSerializer


class RestaurantListView(ListAPIView):
    serializer_class = RestaurantListSerializer
    queryset = Restaurant.objects.all()
