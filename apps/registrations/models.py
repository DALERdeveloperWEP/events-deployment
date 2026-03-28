from django.db import models

from apps.user.models import User
from apps.events.models import Event


class RegistrationStatus(models.TextChoices):
    REGISTERED = 'registered', 'Registered'
    CANCELLED = 'cancelled', 'Cancelled'


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    status = models.CharField(max_length=20, choices=RegistrationStatus.choices)
    registered_at = models.DateTimeField(auto_now_add=True)
    cancelled_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        unique_together = ('user', 'event')