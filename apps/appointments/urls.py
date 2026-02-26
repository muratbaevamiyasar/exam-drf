from django.urls import path
from .views import AppointmentCreateView, MyAppointmentsView

urlpatterns = [
    path("appointments/", AppointmentCreateView.as_view()),
    path("appointments/me/", MyAppointmentsView.as_view()),
]