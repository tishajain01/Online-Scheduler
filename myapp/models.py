# models.py

from django.db import models
from django.contrib.auth.models import User

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, default='') 
    email = models.EmailField(default='')
    department = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL_CHOICES = [
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('ADVANCED', 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.name

class ScheduledLecture(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

    class Meta:
        unique_together = ['instructor', 'date']  # Ensures each instructor can only have one lecture per day
