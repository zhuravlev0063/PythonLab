# court_case/forms.py
from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['case_number', 'title', 'description']

# court_case/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('case/<int:pk>/', views.case_detail, name='case_detail'),
    path('add_case/', views.add_case, name='add_case'),
]
