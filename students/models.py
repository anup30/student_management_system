from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


    
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

    def get_absolute_url(self):
        return reverse('course-list')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    courses = models.ManyToManyField(Course)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})
    
"""
from django.db.models.signals import pre_delete
from django.dispatch import receiver

@receiver(pre_delete, sender=Student)
def delete_user_on_student_delete(sender, instance, **kwargs):
    user = instance.user
    user.delete()
"""