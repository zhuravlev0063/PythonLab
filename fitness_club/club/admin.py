from django.contrib import admin
from .models import Trainer, TrainingSession, Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone', 'email')
    search_fields = ('name', 'specialization')

@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'trainer', 'date')
    list_filter = ('trainer', 'date')
    search_fields = ('title',)
    filter_horizontal = ('clients',)