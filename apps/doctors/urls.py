from django.urls import path
from .views import DoctorListView, TimeSlotCreateView

urlpatterns = [
    path("doctors/", DoctorListView.as_view()),
    path("timeslots/", TimeSlotCreateView.as_view()),
]