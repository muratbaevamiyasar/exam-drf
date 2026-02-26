from rest_framework import serializers
from .models import DoctorProfile, TimeSlot
from django.utils import timezone

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = "__all__"

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = "__all__"

    def validate(self, data):
        doctor = self.context["request"].user
        date = data["date"]
        start = data["start_time"]
        end = data["end_time"]

        if date < timezone.now().date():
            raise serializers.ValidationError("Past date not allowed")

        overlap = TimeSlot.objects.filter(
            doctor=doctor,
            date=date,
            start_time__lt=end,
            end_time__gt=start
        ).exists()

        if overlap:
            raise serializers.ValidationError("Time overlap")

        return data