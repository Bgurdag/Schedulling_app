from django.db import models

#Models for events created
class Event(models.Model):
    eventname = models.CharField(max_length=200)
    start_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.eventname

