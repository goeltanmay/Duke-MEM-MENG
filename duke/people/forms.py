from django import forms
from models import COURSE_CHOICES
from django.core.exceptions import ValidationError
import os

class StudentForm(forms.Form):
    duke_id = forms.IntegerField(label = "Duke ID", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    student_name = forms.CharField(label='Your name', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    description = forms.CharField(label='About You', max_length=142, widget=forms.Textarea(attrs={'class' : 'form-control'}))
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class' : 'form-control'}))
    name_audio = forms.FileField(widget=forms.FileInput(attrs={'class' : 'form-control'}))
    course = forms.ChoiceField(choices = COURSE_CHOICES, widget=forms.Select(attrs={'class' : 'form-control'}))

    def clean_name_audio(self):
    	audio_file = self.cleaned_data['name_audio']
    	if not audio_file.name.endswith(".mp3"):
    		raise ValidationError('Invalid type of file. Only .mp3 file allowed.', code='invalid')
    	return audio_file