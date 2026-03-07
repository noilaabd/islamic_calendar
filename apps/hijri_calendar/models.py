from django.db import models

class Event(models.Model):
    EVENT_TYPES = [
        ('holiday', 'Праздник'),
        ('fasting', 'Пост'),
        ('memorial', 'Памятная дата'),
    ]

    name = models.CharField(max_length=200, verbose_name="Название события")
    description = models.TextField(blank=True, verbose_name="Описание")
    
    gregorian_date = models.DateField(verbose_name="Дата (Григорианская)")
    
    event_type = models.CharField(
        max_length=20, 
        choices=EVENT_TYPES, 
        default='holiday',
        verbose_name="Тип события"
    )

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ['gregorian_date']

    def __str__(self):
        return f"{self.name} ({self.gregorian_date})"
