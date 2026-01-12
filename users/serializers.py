from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ConfirmationCode
from .utils import generate_code


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email"),
            is_active=False
        )

        code = generate_code()
        ConfirmationCode.objects.create(user=user, code=code)

        # пока просто выводим код в консоль
        print("CONFIRM CODE:", code)

        return user


class ConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()
