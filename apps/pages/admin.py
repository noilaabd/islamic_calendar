from django.contrib import admin
from .models import Event, HijriMonth


@admin.register(HijriMonth)
class HijriMonthAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')
    ordering = ('number',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'gregorian_date', 'day_hijri', 'month_hijri')
    list_filter = ('type', 'month_hijri')
    search_fields = ('name', 'description', 'slug')
    ordering = ('gregorian_date',)
    prepopulated_fields = {"slug": ("name",)}