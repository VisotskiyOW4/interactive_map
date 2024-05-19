from django.db import models

class Floor(models.Model):
    id = models.AutoField(primary_key=True)
    floor = models.IntegerField()
    svg = models.FileField(upload_to='svg_files/')

    def __str__(self):
        return f"Floor {self.floor}"

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    svg_path = models.TextField(null=True, default=None)  # Поле для зберігання шляху SVG

    def __str__(self):
        return f"Room {self.room_number} on Floor {self.floor.floor}"

class RoomItem(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    item_number = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return f"Item {self.item_number.item_name} in Room {self.room_number.room_number}"

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    inventory_number = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    specification = models.TextField()
    item_name = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
