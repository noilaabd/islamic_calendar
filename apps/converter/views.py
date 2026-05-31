from django.http import JsonResponse
from django.shortcuts import render
from hijri_converter import Hijri
from datetime import date, datetime

def converter_view(request):
    now = datetime.now()
    backgrounds = ['images/bg1.png', 'images/bg2.png', 'images/bg3.png']
    background = backgrounds[(now.hour // 3) % len(backgrounds)]
    context = {
        'background': background
    }
    return render(request, "converter.html")


def convert_date(request):
    g_date = request.GET.get("gregorian")
    h_date = request.GET.get("hijri")

    if g_date and not h_date:
        y, m, d = map(int, g_date.split("-"))
        h = Hijri.from_gregorian(y, m, d)
        return JsonResponse({
            "result": f"{h.year}-{h.month:02}-{h.day:02}"
        })

    if h_date and not g_date:
        try:
            y, m, d = map(int, h_date.split("-"))
            g = Hijri(y, m, d).to_gregorian()
            return JsonResponse({
                "result": f"{g.year}-{g.month:02}-{g.day:02}"
            })
        except ValueError:
            return JsonResponse({"result": "Неверный формат даты"})

    return JsonResponse({"result": "Заполните только одно поле"})