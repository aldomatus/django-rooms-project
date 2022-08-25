from django.db import models


class Room(models.Model):
    room_id = models.SmallAutoField(primary_key=True)
    is_available = models.BooleanField(null=False, default=False)
    capacity_of_users = models.IntegerField()
    busy_places = models.IntegerField(default=0)
