from events.models import Event
from rooms.models import Room
from rest_framework import serializers

from datetime import datetime


class EventSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(), many=False)
    is_public = serializers.BooleanField()
    event_date = serializers.DateTimeField(default=datetime.now().isoformat())

    class Meta:
        model = Event
        fields = ['room', 'is_public', 'event_date']

    def create(self, validated_data):
        return Event.objects.create(**validated_data)
