from django.db import models
from hijri_converter import Hijri


class DateConverter(models.Model):
    gregorian_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Григорианская дата"
    )

    hijri_date = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Хиджрийская дата (YYYY-MM-DD)"
    )

    result = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Результат конвертации"
    )

    class Meta:
        verbose_name = "Конвертер даты"
        verbose_name_plural = "Конвертеры дат"

    def save(self, *args, **kwargs):
        if self.gregorian_date and not self.hijri_date:
            g = self.gregorian_date
            h = Hijri.from_gregorian(g.year, g.month, g.day)
            self.result = f"{h.year}-{h.month:02}-{h.day:02}"

        elif self.hijri_date and not self.gregorian_date:
            try:
                year, month, day = map(int, self.hijri_date.split("-"))
                g = Hijri(year, month, day).to_gregorian()
                self.result = f"{g.year}-{g.month:02}-{g.day:02}"
            except ValueError:
                self.result = "Неверный формат даты"

        else:
            self.result = "Заполните только одно поле"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.result