from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.pages.urls')),    
    path('calendar/', include('apps.hijri_calendar.urls')), 
    path('converter/', include('apps.converter.urls')), 
    path('events/', include('apps.events.urls')),          
]