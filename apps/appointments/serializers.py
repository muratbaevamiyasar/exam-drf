from rest_framework import serializers
from .models import Appointment
from django.utils import timezone

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

    def validate(self, data):
        timeslot = data["timeslot"]

        if not timeslot.is_available:
            raise serializers.ValidationError("Already booked")

        if timeslot.date < timezone.now().date():
            raise serializers.ValidationError("Past date")

        if self.context["request"].user == timeslot.doctor:
            raise serializers.ValidationError("Doctor cannot book own slot")

        return data

    def create(self, validated_data):
        timeslot = validated_data["timeslot"]
        timeslot.is_available = False
        timeslot.save()
        return super().create(validated_data)