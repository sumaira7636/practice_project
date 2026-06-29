from django.contrib import admin
from .models import *


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("id",)

@admin.register(ServiceCategory)

class ServiceCategoryAdmin(admin.ModelAdmin): 
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)

@admin.register(TechnicianProfile)
class TechnicianProfileAdmin(admin.ModelAdmin):

    list_display = ( "id", "user", "skill", "region", "slot_capacity", "is_available",)
    list_filter = ( "skill", "region", "is_available",)
    search_fields = ("user__username", "region",)
    ordering = ("id",)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ( "id", "customer", "service", "technician", "booking_date", "status", "payment_done",)
    list_filter = ( "status", "service", "booking_date","payment_done",)
    search_fields = ( "customer__username","technician__username","address",)
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ( "id", "booking", "customer", "rating", "created_at",)
    list_filter = ("rating",)
    search_fields = ("customer__username",)
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)

@admin.register(JobProof)
class JobProofAdmin(admin.ModelAdmin):

    list_display = ("id","booking","uploaded_at",)
    readonly_fields = ("uploaded_at",)
    ordering = ("-uploaded_at",)