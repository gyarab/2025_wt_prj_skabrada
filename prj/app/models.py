from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=100)
    hex_id = models.CharField(max_length=7)
    info_misc = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.hex_id})"


class Palette(models.Model):
    name = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    viewed = models.BooleanField(default=False)

    views_count = models.PositiveIntegerField(default=0)

    is_favourite = models.BooleanField(default=False)

    colors = models.ManyToManyField(Color, blank=True)

    def __str__(self):
        return self.name