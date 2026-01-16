from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    ProductViewSet,
    ProductWithReviewsViewSet,
    ReviewViewSet,
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'products-with-reviews', ProductWithReviewsViewSet, basename='products-with-reviews')
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
