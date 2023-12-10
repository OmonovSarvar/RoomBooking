from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.SmallIntegerField()
    booked = models.BooleanField(default=False)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    def str(self):
        return self.name
