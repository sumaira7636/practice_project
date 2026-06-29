from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.permissions import *
from rest_framework.permissions import IsAuthenticated
from ..models import *
from .serializers import *


class ServiceListView(APIView):

    permission_classes = [IsAuthenticated, IsCustomer]
    def get(self, request):
        services = ServiceCategory.objects.all()
        serializer = ServiceCategorySerializer(services,many=True)
        return Response(serializer.data)


class BookingCreateView(APIView):

    permission_classes = [IsAuthenticated, IsCustomer]
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            service = serializer.validated_data["service"]
            address = serializer.validated_data["address"]
            technician = TechnicianProfile.objects.filter(skill=service,region__iexact=address,is_available=True).first()
            booking = serializer.save(customer=request.user)
            if technician:
                booking.technician = technician.user
                booking.status = "Assigned"
                booking.save()
            return Response(BookingListSerializer(booking).data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class MyBookingsView(APIView):

    permission_classes = [IsAuthenticated, IsCustomer]
    def get(self, request):
        bookings = Booking.objects.filter(customer=request.user)
        serializer = BookingListSerializer(bookings,many=True)
        return Response(serializer.data)

class ReviewCreateView(APIView):

    permission_classes = [IsAuthenticated, IsCustomer]
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.validated_data["booking"]
            if booking.customer != request.user:
                return Response({"error":"Not your booking."},status=403)
            if booking.status != "Completed":
                return Response({"error":"Job not completed."},status=400)
            serializer.save(customer=request.user)
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

class TechnicianJobsView(APIView):

    permission_classes = [IsAuthenticated, IsTechnician]
    def get(self, request):
        bookings = Booking.objects.filter(technician=request.user)
        serializer = BookingListSerializer(bookings,many=True)
        return Response(serializer.data)


class StartJobView(APIView):

    permission_classes = [IsAuthenticated, IsTechnician]
    def post(self, request, pk):
        booking = Booking.objects.get(id=pk,technician=request.user)
        booking.status = "Started"
        booking.save()
        return Response({"message":"Job Started"})


class CompleteJobView(APIView):

    permission_classes = [IsAuthenticated, IsTechnician]
    def post(self, request, pk):
        booking = Booking.objects.get(id=pk,technician=request.user)
        booking.status = "Completed"
        booking.save()
        return Response({"message":"Job Completed"})

class UploadProofView(APIView):

    permission_classes = [IsAuthenticated, IsTechnician]
    def post(self, request):
        serializer = JobProofSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
