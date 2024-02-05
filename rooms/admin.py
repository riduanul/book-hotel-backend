from django.contrib import admin
from .models import UserProfile, Hotel, Room, Booking
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
