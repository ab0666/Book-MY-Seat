from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from attendee.models import Event, Queue

def addtoqueues(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            evt_id = int(request.POST.get('event_id'))
            event_check = Event.objects.get(id=evt_id)
            if(event_check):
                if(Queue.objects.filter(user=request.user.id, event_id=evt_id)):
                    return JsonResponse({'status': "Event Already in Queues"})
                else:
                    evt_qty = int(request.POST.get('event_qty'))
                    if event_check.quantity >= evt_qty:
                        Queue.objects.create(user=request.user, event_id=evt_id, event_qty = evt_qty)
                        return JsonResponse({'status': "Event added sucessfully"})
                    else:
                        return JsonResponse({'status': "Only " + str(event_check.quantity) + " Quantity available"})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to Continue"})
        
    return redirect('/')

@login_required(login_url='loginpage')
def viewqueues(request):
    queues = Queue.objects.filter(user=request.user)
    context = {'queues': queues}
    return render(request, "attendee/queues.html", context)

def updatequeues(request):
    if request.method == 'POST':
        evt_id = int(request.POST.get('event_id'))
        if(Queue.objects.filter(user=request.user, event_id=evt_id)):
            evt_qty = int(request.POST.get('event_qty'))
            queue = Queue.objects.get(event_id=evt_id, user=request.user)
            queue.event_qty = evt_qty
            queue.save()
            return JsonResponse({'status': "Updated Successfully"})
        return redirect('/')
    
def deletecartitem(request):
    if request.method == 'POST':
        evt_id = int(request.POST.get('event_id'))
        if(Queue.objects.filter(user=request.user, event_id=evt_id)):
            queueitem= Queue.objects.get(event_id = evt_id, user=request.user)
            queueitem.delete()
            return JsonResponse({'status': "Deleted Successfully"})
        return redirect('/')
