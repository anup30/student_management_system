from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from students.models import Student, Course

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone_number = forms.CharField(max_length=15)
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=True)
        # Create the associated Student object
        student = Student(
            user=user,
            phone_number=self.cleaned_data['phone_number']
        )
        student.save()
        # Add courses
        courses = self.cleaned_data['courses']
        student.courses.set(courses)
        return user