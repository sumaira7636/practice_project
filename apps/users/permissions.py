from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role
            and request.user.role.name == "Customer"
        )


class IsTechnician(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role
            and request.user.role.name == "Technician"
        )


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


# BasePermission?BasePermission is DRF's base class used to create custom authorization rules.
# has_permission()?
# has_permission() is a method that DRF automatically calls before executing a view to determine whether the request should be allowed.

# Authorization

# "What are you allowed to do?"
# Who can do something?
# This is called Authorization.
# Authentication
# "Who are you?"
# Permission:
# A permission is a single action.
# Examples:
# Can add student
# Can update student
# Can delete student
# Can view student

# Role:
# A role is a collection of permissions.
# Example:
# Teacher Role
#  ├── view_student
#  ├── add_assignment
#  ├── mark_attendance


# Complete Flow Diagram
# User Login
#      ↓
# Authentication
#      ↓
# Identify User
#      ↓
# Get User Role
#      ↓
# Get Role Permissions
#      ↓
# User Performs Action
#      ↓
# Check Permission
#      ↓
# Allow or Deny