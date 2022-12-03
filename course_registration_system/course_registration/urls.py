from django.urls import path
from . import views

app_name = 'course_registration'

urlpatterns = [
    path('course/list', views.course_list, name ="course-list"),
    path('course/add', views.course_add, name ="course-add"),
    path('course/list/<course_id>', views.delete_course, name="delete-course"),
    path('add_student/<course_id>', views.add_student, name="add-student"),
    path('dec_student/<course_id>', views.dec_student, name="dec-student"),
]