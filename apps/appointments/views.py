from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentSerializer
from apps.users.permissions import IsPatient, IsAdmin

class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsPatient]

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user, doctor=serializer.validated_data["timeslot"].doctor)

class MyAppointmentsView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.select_related("doctor", "patient", "timeslot").filter(
            patient=user
        )