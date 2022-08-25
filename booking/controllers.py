from booking.models import Booking


def is_user_already_registered(event, user):
    return Booking.objects.filter(event=event, user=user).first()


def get_booking_to_cancel(event, user):
    return Booking.objects.filter(event=event, user=user).first()