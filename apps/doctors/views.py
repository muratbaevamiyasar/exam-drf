from rest_framework import generics
from .models import DoctorProfile, TimeSlot
from .serializers import DoctorProfileSerializer, TimeSlotSerializer
from apps.users.permissions import IsDoctor, IsAdmin
from rest_framework.permissions import AllowAny

class DoctorListView(generics.ListAPIView):
    queryset = DoctorProfile.objects.select_related("user")
    serializer_class = DoctorProfileSerializer
    permission_classes = [AllowAny]
    search_fields = ["specialization", "user__username"]

class TimeSlotCreateView(generics.CreateAPIView):
    serializer_class = TimeSlotSerializer
    permission_classes = [IsDoctor]

    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user)