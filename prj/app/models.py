from django.db import models

class Book(models.Model):
    # id
    title = models.CharField(MAX_lenght=255)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    writter = models.ForeignKey('Writter', on_delete=models.SET_NULL, null=True)

class Writter(models.Model):
    # id
    Name = models.CharField(MAX_lenght=255)
    country = models.PositiveSmallIntegerField(blank=True, null=True)