import sys
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from rooms.serializers import RoomSerializer
from rooms.controllers import get_room_by_id
from events.controllers import room_has_events


class RoomAPIView(APIView):
    """Create an event."""

    def post(self, request, *args, **kwargs):
        try:
            serializer = RoomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            exc_tb = sys.exc_info()[2]
            return Response({"message": "something bad occurred!",
                             "error": f"{str(e)} line: {exc_tb.tb_lineno}"
                             },
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            # Verify the existence of the room
            room = get_room_by_id(request.data["room_id"])

            # Check if the room has any event
            if room_has_events(request.data["room_id"]) is None:
                room.delete()
            else:
                return Response({"message": f"room {request.data['room_id']} has actived events"},
                                status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": f"Deleted room {request.data['room_id']}"},
                            status=status.HTTP_200_OK)

        except Exception as e:
            exc_tb = sys.exc_info()[2]
            return Response({"message": "something bad ocurred!",
                             "error": f"{str(e)} line: {exc_tb.tb_lineno}"
                             },
                            status=status.HTTP_400_BAD_REQUEST)
