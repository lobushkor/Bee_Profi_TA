from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Client, Manager
from django.contrib.auth.models import User


class TourRequest(models.Model):
    country = models.CharField(max_length=100)
    hotel = models.CharField(max_length=100, default='No hotel')
    nights = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(24)], default=7)
    pax = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=2)
    child = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)], default=0)
    client_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    managers = models.ManyToManyField(Manager, related_name='tour_requests', blank=True)
    status = models.CharField(max_length=50, default='не в роботі')

    def __str__(self):
        return f"{self.user.get_full_name()}: {self.client_text[:50]}"


class Destination(models.Model):
    place_name = models.CharField(max_length=50, null=True, blank=True)
    place_description = models.CharField(max_length=200, null=True, blank=True)
