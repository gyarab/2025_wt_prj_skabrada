from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=100)
    hex_id = models.CharField(max_length=7)
    info_misc = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.hex_id})"

class Palete(models.Model):
    name = models.CharField(max_length=255)
    number_of_colors = models.PositiveSmallIntegerField(blank=True, null=True)
    added_to_system = models.DateTimeField(auto_now_add=True)
    added_to_favourites = models.DateTimeField(auto_now_add=True)
    favourited = models.DateTimeField(auto_now_add=True)
    viewed = models.BooleanField(default=False)

    colors = models.ManyToManyField(Color, blank=True) 

    def __str__(self):
        return self.name