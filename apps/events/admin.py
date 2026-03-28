from django.contrib import admin

from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'event_type', 'location')
    search_fields = ('title', 'location')
    ordering = ('id',)