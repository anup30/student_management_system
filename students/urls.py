from django.urls import path
from .views import (
    HomeView, StudentListView, StudentDetailView, StudentCreateView, 
    StudentUpdateView, StudentDeleteView, CourseListView, CourseCreateView,
    CourseUpdateView, CourseDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # Student URLs
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/add/', StudentCreateView.as_view(), name='student-add'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    # Course URLs
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/add/', CourseCreateView.as_view(), name='course-add'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
]
