from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.views import PaymentViewSet, UserCreateAPIView, UserListAPIView

app_name = "users"

router = DefaultRouter()
router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = [
    path("user", UserListAPIView.as_view(), name="user_list"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
] + router.urls
