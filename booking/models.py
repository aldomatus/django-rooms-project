
from django.db import models
from django.utils import timezone

from users.models import User
from events.models import Event


class Booking(models.Model):
    booking_id = models.SmallAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='users_booking', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='events_booking', on_delete=models.CASCADE)
    is_active = models.BooleanField(null=False, default=False)
    event_date = models.DateTimeField(default=timezone.now)