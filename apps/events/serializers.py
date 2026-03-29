from .models import Event, EventType
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("Start time must be before end time.")
        if data['event_type'] == EventType.OFFLINE and not data['location']:
            raise serializers.ValidationError("Location is required for offline events.")
        if data['capacity'] <= 0:
            raise serializers.ValidationError("Capacity must be a positive integer.")
        return data
    
    class Meta:
        model = Event
        fields = '__all__'