import calendar
from datetime import date, datetime
from django.shortcuts import render
from apps.pages.models import Event, HijriMonth 
from hijri_converter import Gregorian

def calendar_view(request):
    today = date.today()
    now = datetime.now()
    
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))
    
    cal = calendar.Calendar(firstweekday=0)
    month_days = cal.monthdatescalendar(year, month)
    
    events = Event.objects.filter(gregorian_date__year=year, gregorian_date__month=month)

    mid_month_date = date(year, month, 15)
    current_h_date = Gregorian(mid_month_date.year, mid_month_date.month, mid_month_date.day).to_hijri()
    month_info = HijriMonth.objects.filter(number=current_h_date.month).first() 

    full_calendar = []
    for week in month_days:
        week_data = []
        for day_date in week:
            if day_date.month != month:
                week_data.append(None)
            else:
                h_date = Gregorian(day_date.year, day_date.month, day_date.day).to_hijri()
                day_events = [e for e in events if e.gregorian_date.day == day_date.day]
                week_data.append({
                    'day': day_date.day,
                    'hijri_day': h_date.day,
                    'events': day_events,
                    'is_today': (day_date == today)
                })
        full_calendar.append(week_data)

    backgrounds = ['images/bg1.png', 'images/bg2.png', 'images/bg3.png']
    background = backgrounds[(now.hour // 3) % len(backgrounds)]

    context = {
        'calendar': full_calendar,
        'month_name': ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
                       "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"][month-1],
        'year': year,
        'month': month,
        'month_info': month_info, 
        'prev_month': month - 1 if month > 1 else 12,
        'prev_year': year if month > 1 else year - 1,
        'next_month': month + 1 if month < 12 else 1,
        'next_year': year if month < 12 else year + 1,
        "background": background, 
    }
    return render(request, 'calendar.html', context)