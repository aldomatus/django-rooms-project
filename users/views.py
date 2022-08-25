import sys
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from users.serializers import UserSerializer


class UserAPIView(APIView):
    """Create a room."""

    def post(self, request, *args, **kwargs):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            exc_tb = sys.exc_info()[2]
            return Response({"message": "something bad ocurred!",
                             "error": f"{str(e)} line: {exc_tb.tb_lineno}"
                             },
                            status=status.HTTP_400_BAD_REQUEST)


class HomeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Welcome to my API"},
                        status=status.HTTP_200_OK)
