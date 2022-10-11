from django.db import models


class MySite(models.Model):
    title = models.CharField("Название", max_length = 50, blank=True)
    content = models.TextField("Описание письма", blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "work request"
        verbose_name_plural = "My works"
        ordering = ['-id']

