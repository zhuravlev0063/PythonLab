from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('case/add/', views.case_add, name='case_add'),
    path('case/edit/<int:pk>/', views.case_edit, name='case_edit'),
    path('case/<int:pk>/', views.case_detail, name='case_detail'),
]
