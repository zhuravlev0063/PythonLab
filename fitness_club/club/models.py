from django.db import models
from datetime import datetime
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта", blank=True)
    phone = models.CharField(max_length=15, verbose_name="Телефон", blank=True)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    specialization = models.CharField(max_length=200, verbose_name="Специализация")
    phone = models.CharField(max_length=15, verbose_name="Телефон", blank=True)
    email = models.EmailField(verbose_name="Электронная почта", blank=True)

    def __str__(self):
        return self.name

class TrainingSession(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название тренировки")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name="Тренер", related_name="sessions")
    date = models.CharField(max_length=100, verbose_name="Дата и время")
    clients = models.ManyToManyField(Client, blank=True, verbose_name="Клиенты")

    def __str__(self):
        return f"{self.title} ({self.date})"