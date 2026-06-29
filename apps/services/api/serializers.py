from rest_framework import serializers
from ..models import *

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = "__all__"

class ServiceCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceCategory
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = [ "id", "service", "region", "address", "booking_date", "booking_time", "payment_done",]
        read_only_fields = ["id"]

class BookingListSerializer(serializers.ModelSerializer):

    service = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    technician = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [ "booking", "rating", "comment",]

class JobProofSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobProof
        fields = [ "booking", "image",]

class TechnicianProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    skill = serializers.StringRelatedField()

    class Meta:
        model = TechnicianProfile
        fields = "__all__"



# imports tools used to convert Django models into JSON format and validate API data.

# A serializer is a translator.It converts:
# Python/Django Objects
#         ↕
# JSON Data
# class Meta:Meta means:Configuration for serializer.
# ModelSerializer automatically generates serializer fields and validation rules based on a Django model.
# fields='all'?It automatically includes all fields from the model in the serialized output.
# serializer.is_valid() do?It validates incoming data against serializer and model rules before saving.
# serializer.save() do?It creates or updates a database record using the validated data.
# Client (Postman)
#        ↓
# JSON Request
#        ↓
# Serializer
#        ↓
# Validation
#        ↓
# Model
#        ↓
# Database

# Database
#        ↓
# Model Object
#        ↓
# Serializer
#        ↓
# JSON Response
#        ↓
# Client