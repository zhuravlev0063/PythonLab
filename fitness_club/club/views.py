from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Trainer, TrainingSession
from .forms import ClientForm, TrainerForm, TrainingSessionForm

# Клиенты
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'club/client_list.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'club/add_client.html', {'form': form})

# Тренеры
def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'club/trainer_list.html', {'trainers': trainers})

def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
    else:
        form = TrainerForm()
    return render(request, 'club/add_trainer.html', {'form': form})

# Тренировки
def training_session_list(request):
    sessions = TrainingSession.objects.all()
    return render(request, 'club/training_session_list.html', {'sessions': sessions})

def add_training_session(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_session_list')
    else:
        form = TrainingSessionForm()
    return render(request, 'club/add_training_session.html', {'form': form})

def home(request):
    return render(request, 'club/home.html')