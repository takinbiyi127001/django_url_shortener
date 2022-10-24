from tabnanny import verbose
from django.db import models
import uuid

# Create your models here.


class Shortener(models.Model):
    """Creates a short url based on an original link

    url: original link
    uuid: shortened link unique id
    created: Time shortened url created
    time_used: Times the shortened url has been used"""

    url = models.URLField()
    uuid = models.CharField(max_length=10, primary_key=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    time_used = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created"]  # order by desc
        verbose_name = "shortener"
        verbose_name_plural = "shorteners"

    def __str__(self):
        return self.url
