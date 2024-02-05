from django.db import models
from django.contrib.auth.models import User

types=[
    ('Deluxe', 'Deluxe'),
    ('Double', 'Double'),
    ('Single', 'Single'),
    ('Kids', 'Kids'),
]
# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(choices = types, max_length=20, null=True, blank=True)
    room_title= models.CharField(max_length=20, blank=True, null=True)
    room_number = models.CharField(max_length=10)
    rent_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)

    def __str__(self):
        return self.room_number

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    num_adults = models.PositiveIntegerField()
    num_children = models.PositiveIntegerField()
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.room.room_number

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username