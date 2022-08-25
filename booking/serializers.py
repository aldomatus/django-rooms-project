from users.models import User
from events.models import Event
from booking.models import Booking
from rest_framework import serializers

from datetime import datetime


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), many=False)
    is_active = serializers.BooleanField()
    event_date = serializers.DateTimeField(default=datetime.now().isoformat())

    class Meta:
        model = Booking
        fields = ['user', 'event', 'is_active', 'event_date']

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)