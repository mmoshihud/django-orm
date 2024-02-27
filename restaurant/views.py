from django.shortcuts import render

from rest_framework.generics import ListAPIView
from restaurant.models import Restaurant

from restaurant.serializers import RestaurantSerializer


class RestaurantListView(ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
