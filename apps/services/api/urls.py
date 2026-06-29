from django.urls import path
from .views import *

urlpatterns = [

    path("services/", ServiceListView.as_view()),
    path("booking/", BookingCreateView.as_view()),
    path("my-bookings/", MyBookingsView.as_view()),
    path("review/", ReviewCreateView.as_view()),
    path("technician/jobs/", TechnicianJobsView.as_view()),
    path("job/start/<int:pk>/", StartJobView.as_view()),
    path("job/complete/<int:pk>/", CompleteJobView.as_view()),
    path("upload-proof/", UploadProofView.as_view()),

]