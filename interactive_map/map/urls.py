from django.urls import path
from .views import map_view, get_room_items

urlpatterns = [
    path('', map_view, name='map'),  # Головна сторінка з мапою
    path('get_room_items/<int:room_number>/', get_room_items, name='get_room_items'),  # API для отримання предметів у кімнаті
]