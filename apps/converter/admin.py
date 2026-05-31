from django.contrib import admin
from .models import DateConverter


@admin.register(DateConverter)
class DateConverterAdmin(admin.ModelAdmin):
    list_display = ("gregorian_date", "hijri_date", "result")
    readonly_fields = ("result",)

    fieldsets = (
        ("Ввод", {
            "fields": ("gregorian_date", "hijri_date"),
        }),
        ("Результат", {
            "fields": ("result",),
        }),
    )