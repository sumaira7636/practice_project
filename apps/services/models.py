from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.users.models import User

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TechnicianProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    skill = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    slot_capacity = models.IntegerField(default=5)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username

class Booking(models.Model):

    STATUS = (
        ("Pending","Pending"),
        ("Assigned","Assigned"),
        ("Started","Started"),
        ("Completed","Completed"),
        ("Cancelled","Cancelled"),
    )
    customer = models.ForeignKey(User,on_delete=models.CASCADE,related_name="customer_bookings")
    technician = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="technician_bookings")
    service = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    address = models.TextField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    status = models.CharField(max_length=20,choices=STATUS,default="Pending")
    payment_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.customer.username}"


class JobProof(models.Model):

    booking = models.OneToOneField(Booking,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="job_proofs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    booking = models.OneToOneField(Booking,on_delete=models.CASCADE)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# imports Django’s database tools
# This gives you tools like:CharField, TextField, BooleanField, DateTimeField
# models.Model = base class of all Django tables
# Each class = one database table
# . (dot):Go inside and access something from it

# null=True	Database	store NULL
# blank=True	Django validation	allow empty input
# Means: User can leave it empty. Database can store it as NULL
#default = False If the user does NOT give any value, store False automatically.
# auto_now=True  The field is automatically updated every time the record is saved (changed).
# _at	timestamp    is_	boolean     _date	date only