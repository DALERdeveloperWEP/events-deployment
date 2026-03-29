from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Event
from .serializers import EventSerializer

class EventViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    
    queryset = Event.objects.all()
    serializer_class = EventSerializer