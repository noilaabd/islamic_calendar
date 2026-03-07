from django.shortcuts import render
from datetime import datetime
from hijri_converter import Gregorian
from .models import Event, HijriMonth
import requests

def home(request):
    now = datetime.now() 

    # григор дата
    time = now.strftime("%H:%M")
    date = now.strftime("%d %B %Y")

    hijri = Gregorian(now.year, now.month, now.day).to_hijri()  # конвертирую в хиджру
    hijri_date = f"{hijri.day} {hijri.month_name()} {hijri.year}"
    current_month_info = HijriMonth.objects.filter(number=hijri.month).first()
    upcoming_events = Event.objects.filter(gregorian_date__gte=now.date()).order_by('gregorian_date')[:5]
    backgrounds = [
        'images/bg1.png',
        'images/bg2.png',
        'images/bg3.png',
    ] 
    background = backgrounds[(now.hour // 3) % len(backgrounds)]

    url = "https://api.aladhan.com/v1/timingsByCity?city=Jalal-Abad&country=Kyrgyzstan&method=3"
    response = requests.get(url).json()

    timings = response['data']['timings']

    prayer_times = {
        "fajr": timings["Fajr"],
        "dhuhr": timings["Dhuhr"],
        "asr": timings["Asr"],
        "maghrib": timings["Maghrib"],
        "isha": timings["Isha"],
    }
 
    context = {
        "time": time, 
        "date": date, 
        "hijri_date": hijri_date,
        "upcoming_events": upcoming_events,
        "background": background, 
        "month_info": current_month_info,
        "prayer_times": prayer_times,

    }

    return render(request, "index.html", context)



# render это функция, которая берет html шаблон, передает туда данные из питона и возращает готовую страницу пользователю
# datetime это встроенный модуль питона для работы со временем и датой (он позволяет видеть текущию дату, время, год, месяц, день)
# now = datetime.now() тут берем текущию дату и время с сервера 
# context данные которые передаются в html
# strftime форматирует дату
# %H часы  %M минуты) пример: 23:30 
# %d день  %B месяц  %Y год) пример: 16 ноябрь 2007

# я установила hijri-converter в терминале