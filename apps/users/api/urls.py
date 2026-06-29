from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from . views import*

urlpatterns = [
    path('signup/',SignupView.as_view(), name='signup'),
    # JWT AUTH
    path('login/',TokenObtainPairView.as_view(),name='login'),
    # Login endpoint for JWT.This generates JWT tokens after login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Refresh token = get new access token without login again.Generates new access token using refresh token
    path('profile/', UserProfileView.as_view(), name='profile'),
    path("update-profile/", UpdateProfileView.as_view(), name="update_profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
]