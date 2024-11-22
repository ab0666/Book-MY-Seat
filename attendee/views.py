from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    trending_event = Event.objects.filter(trending=1)
    category = Category.objects.filter(status=0)
    context = {
        'trending_event': trending_event,
        'category': category
    }
    return render(request, "attendee/index.html", context)

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.error(request, "Your inquiry has been successfully sent. Thank you for reaching out!")
    return render(request, 'attendee/contact.html')


def services(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, "attendee/services.html", context)

def servicesview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        events = Event.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'events': events, 'category':category}
        return render(request, "attendee/events/index.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect('services')

def eventview(request, cate_slug, evt_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Event.objects.filter(slug=evt_slug, status=0)):
            events = Event.objects.filter(slug=evt_slug, status=0).first
            context = {'events' : events}
        else:
            messages.error(request, "No such Product found")
            return redirect('services')
    else:
        messages.error(request, "No such category found")
        return redirect('services')
    return render(request, "attendee/events/view.html", context)