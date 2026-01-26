from rest_framework import serializers
from .models import Category, Product, Review
from rest_framework.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, category):
            return Product.objects.filter(category=category).count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductWithReviewsSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'reviews', 'rating']
        depth = 1

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return round(sum([r.stars for r in reviews]) / reviews.count(), 2)
        return None


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=2, max_length=100)


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=2, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    price = serializers.FloatField(min_value=0.01)
    category = serializers.IntegerField(min_value=1)

    def validate_category(self, category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist')


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, min_length=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    product = serializers.IntegerField(min_value=1)

    def validate_product(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product does not exist')




















# from rest_framework import serializers
# from .models import Category, Product, Review

# class CategorySerializer(serializers.ModelSerializer):
#     products_count = serializers.IntegerField(read_only=True)

#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'products_count')

#     def validate_name(self, value):
#         if len(value.strip()) < 3:
#             raise serializers.ValidationError(
#                 "Название категории должно быть минимум 3 символа"
#             )
#         if any(char.isdigit() for char in value):
#             raise serializers.ValidationError(
#                 "Название категории не должно содержать цифры"
#             )
#         return value

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'

#     def validate_title(self, value):
#         if len(value.strip()) < 3:
#             raise serializers.ValidationError(
#                 "Название товара должно быть минимум 3 символа"
#             )
#         return value

#     def validate_description(self, value):
#         if len(value.strip()) < 10:
#             raise serializers.ValidationError(
#                 "Описание должно быть минимум 10 символов"
#             )
#         return value

#     def validate_price(self, value):
#         if value <= 0:
#             raise serializers.ValidationError(
#                 "Цена должна быть больше 0"
#             )
#         return value


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ('id', 'text', 'stars', 'product')

#     def validate_text(self, value):
#         if len(value.strip()) < 5:
#             raise serializers.ValidationError(
#                 "Текст отзыва должен быть минимум 5 символов"
#             )
#         return value

#     def validate_stars(self, value):
#         if value < 1 or value > 5:
#             raise serializers.ValidationError(
#                 "Оценка должна быть от 1 до 5"
#             )
#         return value

# class ProductWithReviewsSerializer(serializers.ModelSerializer):
#     reviews = ReviewSerializer(many=True, read_only=True)
#     rating = serializers.FloatField(read_only=True)

#     class Meta:
#         model = Product
#         fields = (
#             'id',
#             'title',
#             'description',
#             'price',
#             'category',
#             'reviews',
#             'rating'
#         )
