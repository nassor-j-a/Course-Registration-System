from django import forms 
from django.forms import ModelForm
from .models import Course

class CourseForm(ModelForm):
    
    # course_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Course Title'}))
    # instructor = forms.Select(widget=forms.Select(attrs={'class':'form-control'}))
    # capacity = forms.TextInput(widget=forms.TextInput(attrs={'class':'form-select', 'placeholder':'Input Capacity'}))
    # open_seats = forms.TextInput(widget=forms.TextInput(attrs={'class':'form-select', 'placeholder':'Input Open Seats'}))
    class Meta:
        model = Course
        fields = ['course_title', 'instructor' ]
        labels = {
            'course_title' : '',
            'instructor' : 'Select Instructor',
        }

        widgets = {
            'course_title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Course Title'}),
            'instructor' : forms.Select(attrs={'class':'form-select', 'placeholder':'Select Instructor'}),
        }
