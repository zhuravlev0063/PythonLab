# court_case/admin.py
from django.contrib import admin
from .models import Case, Participant, Hearing

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('case_number', 'title', 'created_at')
    search_fields = ('case_number', 'title')
    list_filter = ('created_at',)

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'case')
    list_filter = ('role',)

@admin.register(Hearing)
class HearingAdmin(admin.ModelAdmin):
    list_display = ('case', 'hearing_date')
    list_filter = ('hearing_date',)
