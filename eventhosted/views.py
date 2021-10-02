from django.shortcuts import render , get_object_or_404
from .models import eventdetails, PostImage

# Create your views here.
def mainpage(request):
    return render(request,"index.html")

def eventpage(request):
    allEvents = eventdetails.objects.all()
    allEvents = list(allEvents)[::-1]
    context = {
    'allEvents':allEvents,
    }
    print(allEvents)
    return render(request,"eventpage.html",context)

def acmevent(request, event_id):
    event = get_object_or_404(eventdetails,id=event_id)
    photos = PostImage.objects.filter(post=event)
    context = {
    'event':event,
    'photos':photos,
    }
    print(photos)
    return render(request,"acmevent1.html",context)
