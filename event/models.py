from django.db import models


class Event(models.Model):
    isComplete = models.BooleanField(default=False)
    user = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=50, blank=False)
    timedate = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
