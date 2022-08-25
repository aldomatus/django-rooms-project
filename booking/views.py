import sys
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from booking.serializers import BookingSerializer
from rooms.controllers import get_room_by_id
from events.controllers import (is_public_event,
                                get_room_id_by_event_id)
from booking.controllers import (is_user_already_registered,
                                 get_booking_to_cancel)


class BookingAPIView(APIView):
    """Create a booking."""

    def post(self, request, *args, **kwargs):
        try:
            serializer = BookingSerializer(data=request.data)

            # User does not register again to the same event
            if is_user_already_registered(request.data["event"], request.data["user"]):
                return Response({"message": f"User is already registered in the event {request.data['event']}"},
                                status=status.HTTP_400_BAD_REQUEST)

            # To verify that it is a public event
            if not is_public_event(request.data["event"]):
                return Response({"message": f"Event {request.data['event']} is not public"},
                                status=status.HTTP_400_BAD_REQUEST)

            # To get the room_id to verify the room it is available
            room_id = get_room_id_by_event_id(request.data["event"])
            room = get_room_by_id(room_id)

            # To validate available places in the room
            if room.is_available and room.capacity_of_users >= room.busy_places + 1:
                room.busy_places = room.busy_places + 1
                room.save()
                if serializer.is_valid():
                    serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            exc_tb = sys.exc_info()[2]
            return Response({"message": "something bad occurred!",
                             "error": f"{str(e)} line: {exc_tb.tb_lineno}"
                             },
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            booking = get_booking_to_cancel(request.data["event"], request.data["user"])
            if booking:
                booking.is_active = 0
                booking.save()
                return Response({"message": f"canceled event {request.data['event']} | user {request.data['user']} "},
                                status=status.HTTP_200_OK)
            else:
                return Response({"message": "record does not exist"},
                                status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(e)
            exc_tb = sys.exc_info()[2]
            return Response({"message": "something bad occurred!",
                             "error": f"{str(e)} line: {exc_tb.tb_lineno}"
                             },
                            status=status.HTTP_400_BAD_REQUEST)
