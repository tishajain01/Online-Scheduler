from django import forms
from .models import Instructor,Course,ScheduledLecture

class ScheduledLectureForm(forms.ModelForm):
    class Meta:
        model = ScheduledLecture
        fields = ['instructor', 'date', 'description']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'phone_number', 'email', 'department','password']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'level', 'description']

