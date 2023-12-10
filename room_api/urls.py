from django.urls import path

from room_api import views

urlpatterns = [
    path('book/<int:room_num>', views.RoomBookingView.as_view(), name='room-booking'),
    path('rooms', views.RoomListView.as_view(), name='room-list'),
    path('rooms/filter', views.RoomFilterView.as_view(), name='room-filter'),
]
