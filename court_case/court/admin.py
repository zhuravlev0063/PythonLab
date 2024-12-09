from django.contrib import admin
from .models import Case, Judge, Lawyer

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('case_number', 'title', 'created_at')
    search_fields = ('case_number', 'title')
    list_filter = ('created_at',)

@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience_years')
    search_fields = ('name',)

@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'case')
    search_fields = ('name',)
