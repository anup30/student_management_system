from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), required=False, help_text="optional if updating")  
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'courses']

    def __init__(self, *args, **kwargs):
        # If we have an instance, populate the initial values
        instance = kwargs.get('instance', None)
        if instance:
            initial = kwargs.get('initial', {})
            initial['username'] = instance.user.username
            initial['first_name'] = instance.user.first_name
            initial['last_name'] = instance.user.last_name
            initial['email'] = instance.user.email
            kwargs['initial'] = initial
        super(StudentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(StudentForm, self).save(commit=False)
        # Create or update associated User object
        if not hasattr(instance, 'user') or not instance.user:
            # Creating a new user
            username = self.cleaned_data['username']
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not password:
                password = 'defaultpassword123'  # Default password, should be changed
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name']
            )
            instance.user = user
        else:
            # Updating existing user
            instance.user.username = self.cleaned_data['username']
            instance.user.first_name = self.cleaned_data['first_name']
            instance.user.last_name = self.cleaned_data['last_name']
            instance.user.email = self.cleaned_data['email']
            
            # Only update password if provided
            if self.cleaned_data['password']:
                instance.user.set_password(self.cleaned_data['password'])
            
            instance.user.save()
        
        if commit:
            instance.save()
            # Save the many-to-many data
            self.save_m2m()
        return instance

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