from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = ( "id","username", "email","phone","role", "is_staff","is_active",)
    list_filter = ("role", "is_staff","is_active",)
    search_fields = ("username","email", "phone",)
    ordering = ("id",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {"fields": ( "phone","address","role",)},),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Information",{"fields": ( "phone","address", "role",)},),
    )


# from django.contrib.auth.admin import UserAdmin:This is extremely important.What is UserAdmin?
# Django already has a ready-made admin configuration for users.It knows how to show:
# Username,Password,Email,Groups,Permissions,Staff Status,Superuser Status,Last Login,Date Joined
# Internally Django has:[class UserAdmin(ModelAdmin)]:which contains hundreds of lines of configuration.Instead of writing everything from scratch:
# [class CustomUserAdmin(UserAdmin): ]inherit it.