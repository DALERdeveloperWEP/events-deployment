from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class EventType(models.TextChoices):
    ONLINE = 'Online', 'Online'
    OFFLINE = 'Offline', 'Offline'
    

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True)
    event_type = models.CharField(max_length=255, choices=EventType.choices)
    location = models.CharField(max_length=124, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)