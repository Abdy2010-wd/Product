from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from .serializers import RegisterSerializer, ConfirmSerializer
from .models import ConfirmationCode


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Пользователь создан. Введите код подтверждения."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmUserView(APIView):
    def post(self, request):
        serializer = ConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        code = serializer.validated_data["code"]

        try:
            user = User.objects.get(username=username)
            confirm = ConfirmationCode.objects.get(user=user, code=code)
        except:
            return Response({"error": "Неверный код"}, status=400)

        user.is_active = True
        user.save()
        confirm.delete()

        return Response({"message": "Пользователь подтверждён"})

