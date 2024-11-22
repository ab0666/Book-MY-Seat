from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from attendee.models import Booking, BookingItem

def index(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, "attendee/bookings/index.html", context)

def viewbooking(request, t_no):
    booking = Booking.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    bookingitems = BookingItem.objects.filter(booking=booking)
    context = {'booking':booking, 'bookingitems': bookingitems}
    return render(request, "attendee/bookings/view.html", context)