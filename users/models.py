from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Введите вашу электронную почту. Используется для входа в систему.",
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Укажите ваш контактный номер телефона (необязательно).",
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Введите название города проживания (необязательно).",
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите изображение для профиля (необязательно).",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.email
