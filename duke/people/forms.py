from django import forms
from models import COURSE_CHOICES

class StudentForm(forms.Form):
    duke_id = forms.IntegerField(label = "Duke ID")
    student_name = forms.CharField(label='Your name', max_length=100)
    picture = forms.ImageField()
    name_audio = forms.FileField()
    course = forms.ChoiceField(choices = COURSE_CHOICES)