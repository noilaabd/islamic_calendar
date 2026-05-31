from django.urls import path
from .views import converter_view, convert_date

urlpatterns = [
    path("", converter_view, name="converter"),
    path("convert/", convert_date, name="convert_date"),
]