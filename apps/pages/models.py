from django.db import models
from django.utils.text import slugify

class Event(models.Model):
    EVENT_TYPES = [
        ('holiday', 'Праздник'), 
        ('fast', 'Пост'), 
        ('memorial', 'Памятная дата')
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True) 
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=EVENT_TYPES, default='memorial')
    day_hijri = models.PositiveSmallIntegerField(default=1) 
    month_hijri = models.PositiveSmallIntegerField(default=1) 
    gregorian_date = models.DateField() 

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name, allow_unicode=True)
            slug = base_slug
            counter = 1
            while Event.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class HijriMonth(models.Model):
    number = models.PositiveSmallIntegerField(unique=True, help_text="Номер от 1 до 12")
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)  # уникальный slug
    description = models.TextField(verbose_name="Описание месяца")
    recommendations = models.TextField(blank=True, verbose_name="Рекомендации (пост, молитвы)")

    def __str__(self):
        return f"{self.number}. {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name, allow_unicode=True)
            slug = base_slug
            counter = 1
            while HijriMonth.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)