from django.contrib import admin

from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event', 'status', 'registered_at', 'cancelled_at')
    search_fields = ('user__username', 'event__title')
    ordering = ('id',)
