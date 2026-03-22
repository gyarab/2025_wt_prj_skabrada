from django.db import models

class Palete(models.Model):
    name = models.CharField(max_length=255)
    number_of_colors = models.PositiveSmallIntegerField(blank=True, null=True)  # snake_case
    added_to_system = models.DateTimeField(auto_now_add=True)
    added_to_favourites = models.DateTimeField(auto_now_add=True)
    favourited = models.DateTimeField(auto_now_add=True)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.name