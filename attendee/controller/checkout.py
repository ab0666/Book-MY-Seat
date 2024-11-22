from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from attendee.models import Queue, Booking, BookingItem, Event

import random

@login_required(login_url='loginpage')
def index(request):
    rawqueue = Queue.objects.filter(user=request.user)
    for item in rawqueue:
        if item.event_qty > item.event.quantity:
            Queue.objects.delete(id=item.id)
    queueitem = Queue.objects.filter(user=request.user)
    total_price = 0
    for item in queueitem:
        total_price = total_price + item.event.selling_price * item.event_qty

    context = {'queueitem': queueitem, 'total_price': total_price}
    return render(request, "attendee/checkout.html", context)

@login_required(login_url='loginpage')
def placebooking(request):
    if request.method == 'POST':
        newbooking = Booking()
        newbooking.user = request.user
        newbooking.fname = request.POST.get('fname')
        newbooking.lname = request.POST.get('lname')
        newbooking.email = request.POST.get('email')
        newbooking.phone = request.POST.get('phone')

        queue = Queue.objects.filter(user=request.user)
        queue_total_price = 0
        for item in queue:
            queue_total_price = queue_total_price + item.event.selling_price * item.event_qty
        newbooking.total_price = queue_total_price
        trackno = "BookMySeat"+str(random.randint(1111111, 9999999))
        while Booking.objects.filter(tracking_no=trackno) is None:
            trackno = "BookMySeat"+str(random.randint(1111111, 9999999))

        newbooking.tracking_no = trackno
        newbooking.save()

        newbookingitems = Queue.objects.filter(user=request.user)
        for item in newbookingitems:
            BookingItem.objects.create(
                booking=newbooking,
                event=item.event,
                price=item.event.selling_price,
                quantity= item.event_qty
            )

            # To decrease the event quantity from available stock
            bookingevent = Event.objects.filter(id=item.event_id).first()
            bookingevent.quantity = bookingevent.quantity - item.event_qty
            bookingevent.save()

        # to clear user queue  
        Queue.objects.filter(user=request.user).delete()

        messages.success(request, "Your booking has been confirmed successfully")
    return redirect('/')


