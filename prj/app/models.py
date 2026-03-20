from django.db import models
from django.contrib.auth.models import User

class Palete(models.Model):
    # id
    Name = models.CharField(max_lenght=255)
    CNumber_Of_Colors = models.PositiveSmallIntegerField(blank=True, null=True)
    Added_To_System = models.PositiveSmallIntegerField(blank=True, null=True)
    Added_To_Favourites = models.PositiveSmallIntegerField(blank=True, null=True)
    Favourited = models.PositiveSmallIntegerField(blank=True, null=True)
    Viewed = models.BooleanField()

    def __str__(self):
        return self.Name