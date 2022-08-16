from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Создайте свои модели здесь.


class UserProfile(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=10, blank=False, default="admin")
    age = models.IntegerField(blank=False, default=100)
    country = models.CharField(max_length=50, blank=False, default="NetherLand")
    city = models.CharField(max_length=50, blank=False, default="Amsterdam")
    name = models.CharField(max_length=50, blank=False, default="Joseph Admin")
    description = models.CharField(max_length=200, blank=False, default="Administration of this city")
    registration_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=200, default="0")
    counts_of_type = models.IntegerField(default=0)

    def __str__(self):
        return self.username
