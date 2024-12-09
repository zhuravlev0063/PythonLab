from django.db import models

class Case(models.Model):
    case_number = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Judge(models.Model):
    name = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    cases = models.ManyToManyField(Case, related_name="judges")

    def __str__(self):
        return self.name

class Lawyer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="lawyers")

    def __str__(self):
        return self.name
