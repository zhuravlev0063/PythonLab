from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django import forms
from django.db import models
from django.urls import path
from django.contrib import admin
from django.apps import AppConfig

# Модели
class Case(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название дела")
    description = models.TextField(verbose_name="Описание")
    date_filed = models.DateField(verbose_name="Дата подачи")

    def __str__(self):
        return self.title


class Judge(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя судьи")
    court_name = models.CharField(max_length=200, verbose_name="Название суда")
    cases = models.ManyToManyField(Case, related_name='judges', verbose_name="Дела")

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя участника")
    role = models.CharField(max_length=50, choices=[
        ('plaintiff', 'Истец'),
        ('defendant', 'Ответчик'),
        ('witness', 'Свидетель'),
    ], verbose_name="Роль")
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='participants', verbose_name="Дело")

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"


# Формы
class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'description', 'date_filed']


# Представления
def case_list(request):
    cases = Case.objects.all()
    return render(request, 'case_list.html', {'cases': cases})


def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    return render(request, 'case_detail.html', {'case': case})


def case_add(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CaseForm()
    return render(request, 'case_form.html', {'form': form})


def case_edit(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CaseForm(instance=case)
    return render(request, 'case_form.html', {'form': form})


# URL маршруты
urlpatterns = [
    path('', case_list, name='case_list'),
    path('<int:pk>/', case_detail, name='case_detail'),
    path('add/', case_add, name='case_add'),
    path('<int:pk>/edit/', case_edit, name='case_edit'),
]


# Админка
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_filed', 'description')
    list_filter = ('date_filed',)
    search_fields = ('title',)


class JudgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'court_name')
    list_filter = ('court_name',)
    search_fields = ('name',)


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'case')
    list_filter = ('role', 'case')
    search_fields = ('name',)


# Конфигурация приложения
class CasesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cases'


# Регистрация в админке
admin.site.register(Case, CaseAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Participant, ParticipantAdmin)
