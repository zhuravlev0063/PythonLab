from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('clients/', views.client_list, name='client_list'),
    path('add-client/', views.add_client, name='add_client'),
    path('trainers/', views.trainer_list, name='trainer_list'),
    path('add-trainer/', views.add_trainer, name='add_trainer'),
    path('sessions/', views.training_session_list, name='training_session_list'),
    path('add-session/', views.add_training_session, name='add_training_session'),
]