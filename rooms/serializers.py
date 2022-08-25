from rooms.models import Room
from rest_framework import serializers


class RoomSerializer(serializers.Serializer):
    capacity_of_users = serializers.IntegerField()
    busy_places = serializers.IntegerField()
    is_available = serializers.BooleanField()

    def create(self, validated_data):
        return Room.objects.create(**validated_data)