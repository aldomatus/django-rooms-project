import sys

from django.core import serializers

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from events.serializers import EventSerializer
from events.controllers import room_with_same_date, get_all_public_events


class EventsAPIView(APIView):
    """Create an event."""

    def post(self, request, *args, **kwargs):
        try:
            serializer = EventSerializer(data=request.data)
            if serializer.is_valid():

                #  Check if there are events already booked for the same room id
                num_events = room_with_same_date(request.data)

                if num_events == 0:
                    serializer.save()
                else:
                    return Response(
                        {"message": f"Room {request.data['room']} not available"},
                        status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            exc_tb = sys.exc_info()[2]
            return Response({"message": "something bad occurred!",
                             "error": f"{str(e)} line: {exc_tb.tb_lineno}"
                             },
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            public_events = get_all_public_events()
            data = serializers.serialize("python", public_events)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            exc_tb = sys.exc_info()[2]
            return Response({"message": "something bad occurred!",
                             "error": f"{str(e)} line: {exc_tb.tb_lineno}"
                             },
                            status=status.HTTP_400_BAD_REQUEST)