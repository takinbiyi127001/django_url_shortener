from django.contrib import admin
from .models import Shortener

# Register your models here.


class ShortenerAdmin(admin.ModelAdmin):
    list_display = (
        "url",
        "uuid",
        "created",
        "time_used",
    )


admin.site.register(Shortener, ShortenerAdmin)
