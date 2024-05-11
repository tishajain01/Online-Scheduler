from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Instructor,Course,ScheduledLecture
from .forms import InstructorForm,CourseForm,ScheduledLectureForm
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate using both username and password
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:  # If the user is a superuser
                return redirect('instructor_list')
            else:  # If the user is an instructor
                return redirect('lecture_list')
    return render(request, 'login.html')

@login_required
def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructor_list.html', {'instructors': instructors})


@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course')
    else:
        form = CourseForm()

    courses = Course.objects.all()
    return render(request, 'add_course.html', {'form': form, 'courses': courses})

def register(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = InstructorForm()
    return render(request, 'register.html', {'form': form})


def schedule_lecture(request, course_id):
    course = Course.objects.get(pk=course_id)
    scheduled_lectures = ScheduledLecture.objects.filter(course_id=course_id)

    if request.method == 'POST':
        form = ScheduledLectureForm(request.POST)
        if form.is_valid():
            scheduled_lecture = form.save(commit=False)

            # Check if the instructor is already scheduled for a lecture on the same date
            existing_lecture = ScheduledLecture.objects.filter(
                instructor=scheduled_lecture.instructor,
                date=scheduled_lecture.date
            ).exclude(course_id=course_id).exists()

            if existing_lecture:
                # If the instructor is already scheduled for another course on the same date
                form.add_error('date', 'This instructor is already scheduled for another lecture on the same date.')
            else:
                # If the instructor is not scheduled for another lecture on the same date
                scheduled_lecture.course = course
                scheduled_lecture.save()
                return redirect('schedule_lecture', course_id=course_id)
    else:
        form = ScheduledLectureForm()

    return render(request, 'schedule_lecture.html', {'form': form, 'scheduled_lectures': scheduled_lectures})

@login_required
def lecture_list(request):
    # Retrieve the current logged-in instructor
    instructor = request.user.instructor

    # Retrieve the scheduled lectures associated with the current instructor
    scheduled_lectures = ScheduledLecture.objects.filter(instructor=instructor)

    return render(request, 'lecture_list.html', {'scheduled_lectures': scheduled_lectures})