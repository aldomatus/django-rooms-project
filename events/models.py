from django.db import models
from django.utils import timezone

from rooms.models import Room


class Event(models.Model):
    event_id = models.SmallAutoField(primary_key=True)
    room = models.ForeignKey(Room, related_name='rooms', on_delete=models.CASCADE)
    is_public = models.BooleanField(null=False, default=False)
    event_date = models.DateTimeField(default=timezone.now)

