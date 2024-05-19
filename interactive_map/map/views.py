from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Room, RoomItem, Floor

def map_view(request):
    floors = Floor.objects.all()
    rooms = Room.objects.all()
    return render(request, 'map/map.html', {'rooms': rooms, 'floors': floors})

def get_room_items(request, room_number):
    room = get_object_or_404(Room, room_number=room_number)
    room_items = RoomItem.objects.filter(room_number=room)
    items = []
    for room_item in room_items:
        item = room_item.item_number
        items.append({
            'item_number': item.id,
            'item_name': item.item_name,
            'specification': item.specification,
            'category_name': item.category.category_name,
        })
    return JsonResponse({'items': items})
