from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Student, Course
from .forms import StudentForm, CourseForm


class HomeView(TemplateView):
    template_name = 'students/home.html'


class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'


class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_message = "Student was added successfully!"


class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_message = "Student information was updated successfully!"

"""
class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
    success_message = "Student was deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
"""
#"""
from django.shortcuts import redirect
from django.contrib.auth.models import User #---
class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
    success_message = "Student was deleted successfully!"

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        user = student.user
        messages.success(self.request, self.success_message)        
        user.delete() 
        return redirect(self.success_url)
#"""

"""
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User #---
class StudentDeleteView(DeleteView):
    model = User
    #model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
    def form_valid(self, form):
        user = self.get_object()
        user.delete()
        messages.error(self.request, "Student Entry has been deleted!")
        return super().form_valid(form)
"""

class CourseListView(ListView):
    model = Course
    template_name = 'students/course_list.html'
    context_object_name = 'courses'


class CourseCreateView(SuccessMessageMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'students/course_form.html'
    success_message = "Course was added successfully!"


class CourseUpdateView(SuccessMessageMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'students/course_form.html'
    success_message = "Course was updated successfully!"


class CourseDeleteView(SuccessMessageMixin, DeleteView):
    model = Course
    template_name = 'students/course_confirm_delete.html'
    success_url = reverse_lazy('course-list')
    success_message = "Course was deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)