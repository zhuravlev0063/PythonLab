from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_list, name='case_list'),
    path('case/<int:pk>/', views.case_detail, name='case_detail'),
    path('case/edit/<int:pk>/', views.case_form, name='case_edit'),
    path('case/new/', views.case_form, name='case_new'),
]
