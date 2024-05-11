from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),  # Default URL redirects to login page
    
    path('register/', views.register, name='register'),  # URL for registration
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('add-course/', views.add_course, name='add_course'),
    path('schedule_lecture/<int:course_id>/', views.schedule_lecture, name='schedule_lecture'),
    path('lecture-list/', views.lecture_list, name='lecture_list'),

]