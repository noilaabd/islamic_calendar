import requests
from django.shortcuts import render
from datetime import datetime



def get_current_background():
    now = datetime.now()
    backgrounds = ['images/bg1.png', 'images/bg2.png', 'images/bg3.png']
    return backgrounds[(now.hour // 3) % len(backgrounds)]


def quran_list_view(request):
    url = "https://api.alquran.cloud/v1/surah"
    try:
        responce = requests.get(url).json()
        surahs = responce['data']
    except Exception:
        surahs = []

    context = {
        'surahs': surahs,
        'background': get_current_background()
    }
    return render(request, "quran_list.html", context)


def quran_detail_view(request, surah_number):
    ar_url = f"https://api.alquran.cloud/v1/surah/{surah_number}"
    tr_url = f"https://api.alquran.cloud/v1/surah/{surah_number}/ru.transliteration"

    surah_data = {}
    try:
        ar_res = requests.get(ar_url).json()['data']
        tr_res = requests.get(tr_url).json()['data']

        ayahs = []
        for i in range(len(ar_res['ayahs'])):
            ayahs.append({
                'number': ar_res['ayahs'][i]['numberInSurah'],
                'arabic': ar_res['ayahs'][i]['text'],
                'transliteration': tr_res['ayahs'][i]['text']
            })
            
        surah_data = {
            'number': ar_res['number'],
            'name': ar_res['englishName'],
            'local_name': ar_res['name'],
            'ayahs': ayahs
        }
    except Exception as e:
        print(f"Ошибка загрузки: {e}")

    context = {
        'surah': surah_data,
        'background': get_current_background()
    }
    return render(request, "quran_detail.html", context)