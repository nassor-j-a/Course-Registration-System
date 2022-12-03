from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_title = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField(default=30)
    open_seats = models.PositiveIntegerField(default=30)
    

    def __str__(self):
        return self.course_title
    
