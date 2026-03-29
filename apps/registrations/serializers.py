from rest_framework import serializers

from apps.registrations.models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    registered_at = serializers.DateTimeField(read_only=True)
    cancelled_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Registration
        fields = '__all__'
        
    def validate(self, data):
        user = data.get('user')
        event = data.get('event')
        
        if not user:
            raise serializers.ValidationError("User is required.")
        
        if data.get('status') != 'cancelled' and data.get('status') != 'registered':
            raise serializers.ValidationError("Invalid status.")
        
        if data.get('status') == 'registered' and Registration.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("User is already registered for this event.")
        
        if data.get('status') == 'cancelled' and not Registration.objects.filter(user=user, event=event, status='registered').exists():
            raise serializers.ValidationError("User is not registered for this event.")
        
        if not event:
            raise serializers.ValidationError("Event is required.")
        
        if Registration.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("User is already registered for this event.")
        
        return data