from django.db import models


class ShortUrl(models.Model):
    counter = models.IntegerField(default=0)
    short_url = models.CharField(max_length=200, unique=True, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

