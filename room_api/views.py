from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework import generics

from .models import Room
from .serializers import RoomSerializer


class RoomBookingView(APIView):
    def post(self, request, room_num):
        try:
            room = Room.objects.get(room_number=room_num)
        except Room.DoesNotExist:
            return Response({"message": "Xona topilmadi yoki mavjud emas xona raqami kiritildi!"},
                            status=status.HTTP_404_NOT_FOUND)

        if room.booked:
            return Response({
                "message": "Xona allaqachon boshqa bir mijoz tomonidan band qilingan!",
                "available_from": room.booked_till.strftime("%Y-%m-%d %H:%M:%S")
            }, status=status.HTTP_409_CONFLICT)

        room.booked = True
        room.booked_from = datetime.now()
        room.booked_till = room.booked_from
        room.save()

        return Response({
            "message": "Xona allaqachon boshqa bir mijoz tomonidan band qilingan!",
            "room": room.name,
            "start": room.booked_from.strftime("%Y-%m-%d %H:%M:%S"),
            "end": room.booked_till.strftime("%Y-%m-%d %H:%M:%S")
        }, status=status.HTTP_201_CREATED)


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomFilterView(APIView):
    def get(self, request):
        day = request.query_params.get('day')
        month = request.query_params.get('month')

        if day and month:
            return Response({
                "message": "Filtered rooms based on day and month",
                "date": f"{month}-{day}"
            }, status=status.HTTP_200_OK)
        else:
            rooms = Room.objects.all()
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
