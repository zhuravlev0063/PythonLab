# court_case/models.py
from django.db import models

class Case(models.Model):
    case_number = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.case_number} - {self.title}"

class Participant(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=[('Plaintiff', 'Истец'), ('Defendant', 'Ответчик')])
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='participants')

    def __str__(self):
        return f"{self.name} ({self.role})"

class Hearing(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='hearings')
    hearing_date = models.DateTimeField()
    summary = models.TextField()

    def __str__(self):
        return f"Hearing for {self.case.case_number} on {self.hearing_date}"
