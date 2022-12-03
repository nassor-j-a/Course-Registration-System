from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Instructor)
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 25


# admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_title', 'instructor', 'capacity', 'open_seats')
    search_fields = ('course_title', 'instructor')
    ordering = ('id',)
    list_per_page = 25