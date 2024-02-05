from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import UserProfileSerializer, HotelSerializer, RoomSerializer, BookingSerializer
from .models import Hotel, Room, Booking, UserProfile
# Create your views here.
class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomListByTypeAPIView(ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        room_type = self.kwargs.get('room_type')
        print(f"Fetching rooms for type: {room_type}")
        queryset = Room.objects.filter(room_type=room_type)
        return queryset

class RoomDetailsApiView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field= 'id'


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserBookingsListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class CancelBookingView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        booking = self.get_object()
        if booking.user == request.user:
            booking.is_cancelled = True
            booking.save()
            return Response({'detail': 'Booking cancelled successfully.'})
        else:
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile