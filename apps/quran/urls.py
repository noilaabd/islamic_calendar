from django.urls import path
from . import views

urlpatterns = [
    path('', views.quran_list_view, name='quran_list'),
    path('<int:surah_number>/', views.quran_detail_view, name='surah_detail'),
]