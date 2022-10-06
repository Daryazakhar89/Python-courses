from django.db import models


class MySite(models.Model):
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')

    class Meta:
        verbose_name = "My work"
        verbose_name_plural = "My works"

