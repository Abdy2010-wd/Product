from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'products_count')

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Название категории должно быть минимум 3 символа"
            )
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                "Название категории не должно содержать цифры"
            )
        return value

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Название товара должно быть минимум 3 символа"
            )
        return value

    def validate_description(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "Описание должно быть минимум 10 символов"
            )
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Цена должна быть больше 0"
            )
        return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'stars', 'product')

    def validate_text(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError(
                "Текст отзыва должен быть минимум 5 символов"
            )
        return value

    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Оценка должна быть от 1 до 5"
            )
        return value

class ProductWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'price',
            'category',
            'reviews',
            'rating'
        )



