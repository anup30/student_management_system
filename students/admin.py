from django.contrib import admin
from .models import Student, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'get_email', 'phone_number', 'get_course_count')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'phone_number')
    filter_horizontal = ('courses',)

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_full_name.short_description = 'Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_course_count(self, obj):
        return obj.courses.count()
    get_course_count.short_description = 'Courses'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'get_student_count')
    search_fields = ('name', 'code', 'description')

    def get_student_count(self, obj):
        return obj.student_set.count()
    get_student_count.short_description = 'Students'