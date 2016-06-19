from __future__ import unicode_literals

import os

from django.db import models
from duke.settings import MEDIA_ROOT

# Choices of Courses - Add here if you want to increase

COURSE_CHOICES = (
    (1, 'MEM'),
    (2, 'MENG'),
)

# Create your models here.

def validate_file_extension(value):
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.mp3','.wav']
	if not ext in valid_extensions:
		raise ValidationError(u'File not supported!')

class Student(models.Model):
	duke_id = models.CharField(max_length = 20, null=False, blank=False)
	student_name = models.CharField(max_length = 200, null=False, blank=False)
	course = models.IntegerField(choices = COURSE_CHOICES, null=False, blank=False)
	description  = models.CharField(max_length = 142)
	picture = models.ImageField()
	name_audio = models.FileField(validators=[validate_file_extension])

	def __unicode__(self):
		return self.student_name
