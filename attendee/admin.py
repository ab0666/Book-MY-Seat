from django.contrib import admin

from .models import Category, Event, Contact, Queue, Booking, BookingItem

# Register your models here.

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(Queue)
admin.site.register(Booking)
admin.site.register(BookingItem)