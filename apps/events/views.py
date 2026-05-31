from django.shortcuts import render
from apps.pages.models import Event 
from datetime import datetime


def events_list(request):
    events = Event.objects.all().order_by('gregorian_date')
    now = datetime.now()
    backgrounds = ['images/bg1.png', 'images/bg2.png', 'images/bg3.png']
    background = backgrounds[(now.hour // 3) % len(backgrounds)]


    context = {
        'events': events,
        "background": background, 
    }
    return render(request, 'events.html', context)