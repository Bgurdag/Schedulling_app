from django.db import models

# Create your models here.
class Event(models.Model):
    eventname = models.CharField(max_length=200)
    date = models.IntegerField
    time
    duration
