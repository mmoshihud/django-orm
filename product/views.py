from django.db.models import Prefetch
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, F

from .models import (
    AttributeValue,
    Category,
    Product,
    ProductImage,
    ProductLine,
    Attribute,
)
from rest_framework.generics import ListAPIView
from .serializers import (
    CategorySerializer,
    ProductCategorySerializer,
    ProductSerializer,
    ProductListSerializer,
)
from django.db import connection, reset_queries


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all categories
    """

    queryset = Category.objects.all().is_active()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductListView(ListAPIView):
    # queryset = Product.objects.all()
    queryset = (
        Product.objects.select_related("category", "product_type")
        .prefetch_related(
            "product_line__product_image",
            "product_line__attribute_value__attribute",
            "attribute_value__attribute",
        )
        .all()
    )
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response


class ProductDetailViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all products
    """

    queryset = Product.objects.all().is_active()

    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(
            self.queryset.filter(slug=slug)
            .prefetch_related(Prefetch("attribute_value__attribute"))
            .prefetch_related(Prefetch("product_line__product_image"))
            .prefetch_related(Prefetch("product_line__attribute_value__attribute")),
            many=True,
        )
        data = Response(serializer.data)

        return data

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<slug>[\w-]+)",
    )
    def list_product_by_category_slug(self, request, slug=None):
        """
        An endpoint to return products by category
        """
        serializer = ProductCategorySerializer(
            self.queryset.filter(category__slug=slug)
            .prefetch_related(
                Prefetch("product_line", queryset=ProductLine.objects.order_by("order"))
            )
            .prefetch_related(
                Prefetch(
                    "product_line__product_image",
                    queryset=ProductImage.objects.filter(order=1),
                )
            ),
            many=True,
        )
        return Response(serializer.data)
