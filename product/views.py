from rest_framework import viewsets
from django.db.models import Avg, Count

from .models import Category, Product, Review
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductWithReviewsSerializer,
    ReviewSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.annotate(
        products_count=Count('products')
    )
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductWithReviewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.annotate(
        rating=Avg('reviews__stars')
    )
    serializer_class = ProductWithReviewsSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer




