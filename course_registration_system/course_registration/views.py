from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import CourseForm
from django.http import HttpResponseRedirect


@login_required(login_url='/login')
# Create your views here.
def course_list(request):
    
    course_details = Course.objects.all()
    return render(request, 'course_registration/course_list.html', {'course_details': course_details})



def course_add(request):
    submitted = False
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/course/list?submitted=True')
    else:
        form = CourseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'course_registration/course_add.html',
                    {'form': form, 'submitted': submitted})

def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('course_registration:course-list')

def add_student(request, course_id):
    # update
    course = Course.objects.get(id=course_id)
    
    open_seat = Course.objects.get(id=course_id).open_seats
    if open_seat > 0:
        decrement_seat = open_seat - 1
        course.open_seats = decrement_seat
        course.save()
        return render(request, 'course_registration/student_added.html')
    else:
        return render(request, 'course_registration/class_full.html')
    

def dec_student(request, course_id):
    # update
    course = Course.objects.get(id=course_id)
    
    open_seat = Course.objects.get(id=course_id).open_seats
    if open_seat == 30:
        return render(request, 'course_registration/no_students.html')
        
    else:
        increament_seat = open_seat + 1
        course.open_seats = increament_seat
        course.save()
        return render(request, 'course_registration/student_dropped.html')
