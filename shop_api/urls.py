from django.contrib import admin
from django.urls import path
from product.views import (
    CategoryListCreateView,
    CategoryDetailView,
    ProductListCreateView,
    ProductDetailView,
    ProductWithReviewsView,
    ReviewListCreateView,
    ReviewDetailView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', CategoryListCreateView.as_view()),
    path('api/v1/categories/<int:pk>/', CategoryDetailView.as_view()),
    path('api/v1/products/', ProductListCreateView.as_view()),
    path('api/v1/products/<int:pk>/', ProductDetailView.as_view()),
    path('api/v1/products/reviews/', ProductWithReviewsView.as_view()),
    path('api/v1/reviews/', ReviewListCreateView.as_view()),
    path('api/v1/reviews/<int:pk>/', ReviewDetailView.as_view()),
]


