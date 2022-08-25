from django.contrib import admin
from django.urls import path

from users.views import UserAPIView, HomeAPIView
from rooms.views import RoomAPIView
from events.views import EventsAPIView
from booking.views import BookingAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeAPIView.as_view(), name='home'),
    path('users/signup/', UserAPIView.as_view(), name='signup'),
    path('rooms/create/', RoomAPIView.as_view(), name='create_rooms'),
    path('rooms/delete/', RoomAPIView.as_view(), name='delete_rooms'),
    path('events/create/', EventsAPIView.as_view(), name='create_events'),
    path('events/', EventsAPIView.as_view(), name='get_events'),
    path('booking/create/', BookingAPIView.as_view(), name='create_booking'),
    path('booking/cancel/', BookingAPIView.as_view(), name='cancel_booking')
]
