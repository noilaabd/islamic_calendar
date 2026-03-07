from django.shortcuts import render

def events_list(request):
    return render(request, 'events/events.html') 
