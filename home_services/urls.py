"""
URL configuration for home_services project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# urls.py:This is the entry point router of your entire backend.It decides:Which URL goes to which system
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from django_otp.admin import OTPAdminSite

# Admin panel ko 2FA se lock karne ke liye
# replaces default admin with OTP-secured admin
# Now admin login becomes:Username + Password + OTP required.NOT just password.

admin.site.__class__ = OTPAdminSite
# Direct package ke views import karein taake valid path() ban sakein
from two_factor.urls import urlpatterns as two_factor_urls

urlpatterns = [
    path('', include(two_factor_urls)),
    # Attach all URLs provided by django-two-factor-auth at root level.This enables full 2FA authentication system UI.This package provides:login page,OTP verification page,QR setup page,
    # backup codes,2FA flow. /account/login/,/account/two_factor/setup/,/account/two_factor/qr/,/account/logout/
    path('admin/', admin.site.urls),
    # Django admin panel route
    path('api/users/', include('apps.users.api.urls')),
    path("api/services/",include("apps.services.api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# from django.contrib import admin:This imports Django's built-in Admin Panel.Django provides a ready-made dashboard where you can:
# Create users,Edit users,Delete users,Manage tasks,Manage groups,Manage permissions
# Without this import:  path('admin/', admin.site.urls)  will not work.
# from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,):These views come from Simple JWT package.
# from django_otp.admin import OTPAdminSite:Normally Django Admin uses: (AdminSite)But OTP package provides: (OTPAdminSite)which supports:Username,
# Password,OTP Code.   instead of only: Username,Password
# from two_factor.urls import urlpatterns as two_factor_urls:Inside the two_factor package there is a file:
# two_factor/urls.py     It contains many URLs like:
# /account/login/
# /account/logout/
# /account/two_factor/setup/
# /account/two_factor/qrcode/