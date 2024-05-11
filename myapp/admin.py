from django.contrib import admin
from .models import Instructor,Course,ScheduledLecture

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(ScheduledLecture)