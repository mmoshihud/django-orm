from rest_framework.generics import ListAPIView, RetrieveAPIView
from restaurant.models import Menu, Restaurant, Review

from restaurant.serializers import RestaurantDetailSerializer, RestaurantListSerializer
from django.db.models import (
    Prefetch,
    OuterRef,
    Subquery,
    Sum,
    Count,
    Case,
    When,
    Value,
    IntegerField,
    CharField,
    TextField,
    Avg,
    F,
    ExpressionWrapper,
    FloatField,
    Q,
)


class RestaurantListView(ListAPIView):
    serializer_class = RestaurantListSerializer
    queryset = (
        Restaurant.objects.select_related("restautant_type")
        .prefetch_related(
            "order_set__orderitem_set__menu_item__menu_item_type",
            # "review_set",
            Prefetch(
                "review_set",
                queryset=Review.objects.filter(rating__gte=3),
                to_attr="good_reviews",
            ),
            "contact_set",
            "menu_set__dish",
            "menu_set__dish__ingredients",
            "menu_set__menuitem_set__menu_item_type",
        )
        .annotate(
            total_reviews=Count("review__id"),
            good_reviews_count=Count(
                Case(
                    When(review__rating__gte=3, then=1),
                    output_field=IntegerField(),
                )
            ),
            bad_reviews_count=Count(
                Case(
                    When(review__rating__lte=2, then=1),
                    output_field=IntegerField(),
                )
            ),
            average_rating=Avg("review__rating"),
        )[:1]
    )

    # for restaurant in queryset:
    #     # Access all reviews for the restaurant
    #     print(type(restaurant.bad_reviews_count))

    # for restaurant in queryset:
    #     # Access all reviews for the restaurant
    #     all_reviews = restaurant.review_set.all()

    #     # Access only "good reviews" using the custom attribute
    #     good_reviews = restaurant.good_reviews

    #     print(type(all_reviews))
    #     print(type(good_reviews))

    #     print(all_reviews)
    #     print(good_reviews)

    #     # Print the results
    #     print("All Reviews:")
    #     for review in all_reviews:
    #         print(f"Review ID: {review.id}, Rating: {review.rating}")

    #     print("\nGood Reviews:")
    #     for good_review in good_reviews:
    #         print(f"Good Review ID: {good_review.id}, Rating: {good_review.rating}")

    # restaurant_category=Case(
    #             When(
    #                 review__rating__gt=3,
    #                 then=Value("Excellent", output_field=CharField(max_length=10)),
    #             ),
    #             When(
    #                 review__rating__lt=2,
    #                 then=Value("Poor", output_field=CharField(max_length=10)),
    #             ),
    #             default=Value("Average", output_field=CharField(max_length=10)),
    #             output_field=CharField(max_length=10),
    #         ),

    # queryset = Restaurant.objects.all()

    # queryset = Restaurant.objects.select_related("restautant_type").prefetch_related(
    #     "menu_set__dish__ingredients",
    #     "menu_set__menuitem_set__menu_item_type",
    #     "order_set",
    #     "order_set__orderitem_set__menu_item__menu_item_type",
    #     "review_set",
    #     "contact_set",
    # )

    # queryset = Restaurant.objects.filter(pk=1).select_related(
    #     "restautant_type"
    # ) # This is how you can optimize to use select_related is enough if queryset returns only one object

    # After all if you put same data in 2 serializer there will be obhiously 2 similer query occur. So, optimize serializer first then optimize queryset


class RestaurantDetailView(RetrieveAPIView):
    serializer_class = RestaurantDetailSerializer

    def get_object(self):
        # here select_related is enough because get object returns only one object
        restaurant = Restaurant.objects.select_related("restautant_type").get(
            pk=self.kwargs["pk"]
        )
        return restaurant
