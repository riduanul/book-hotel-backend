from django.urls import path
from .views import RoomDetailsApiView, RoomListCreateView, BookingListCreateView,CancelBookingView, RoomListByTypeAPIView

urlpatterns = [
   
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/by_type/<str:room_type>/', RoomListByTypeAPIView.as_view(), name='room-list-by-type'),
    path('rooms/<int:id>/', RoomDetailsApiView.as_view(), name='room-details'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/cancel/<int:pk>/', CancelBookingView.as_view(), name='cancel-booking'),
]
