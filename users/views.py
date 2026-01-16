from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User

from .serializers import RegisterSerializer, ConfirmSerializer
from .models import ConfirmationCode


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Пользователь создан. Введите код подтверждения."},
            status=status.HTTP_201_CREATED
        )


class ConfirmUserView(GenericAPIView):
    serializer_class = ConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        code = serializer.validated_data["code"]

        try:
            user = User.objects.get(username=username)
            confirm = ConfirmationCode.objects.get(user=user, code=code)
        except (User.DoesNotExist, ConfirmationCode.DoesNotExist):
            return Response({"error": "Неверный код"}, status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()
        confirm.delete()

        return Response({"message": "Пользователь подтверждён"}, status=status.HTTP_200_OK)


