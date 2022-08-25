from users.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    is_admin = serializers.BooleanField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)