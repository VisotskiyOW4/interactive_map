from django.contrib import admin
from .models import Floor, Room, RoomItem, Item, Category

admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(RoomItem)
admin.site.register(Item)
admin.site.register(Category)
