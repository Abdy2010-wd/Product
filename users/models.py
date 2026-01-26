from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import CustomUserManager
from django.core.exceptions import ValidationError

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # добавлено поле
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def clean(self):
        # phone_number обязателен только для суперпользователя
        if self.is_superuser:
            if not self.phone_number:
                raise ValidationError("Суперпользователь должен указать номер телефона.")
            if not self.phone_number.startswith("+996"):
                raise ValidationError("Номер телефона суперпользователя должен начинаться с +996.")

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.email


class ConfirmationCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='confirmation_code')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Код подтверждения для {self.user.email}"

       




