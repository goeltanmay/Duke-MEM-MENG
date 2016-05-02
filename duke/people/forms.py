from django import forms
from models import COURSE_CHOICES

class StudentForm(forms.Form):
    duke_id = forms.IntegerField(label = "Duke ID", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    student_name = forms.CharField(label='Your name', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class' : 'form-control'}))
    name_audio = forms.FileField(widget=forms.FileInput(attrs={'class' : 'form-control'}))
    course = forms.ChoiceField(choices = COURSE_CHOICES, widget=forms.Select(attrs={'class' : 'form-control'}))