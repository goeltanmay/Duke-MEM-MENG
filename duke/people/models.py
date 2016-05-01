from __future__ import unicode_literals

from django.db import models

# Choices of Courses - Add here if you want to increase

COURSE_CHOICES = (
    (1, 'MEM'),
    (2, 'MENG'),
)

# Create your models here.

class Student(models.Model):
	duke_id = models.CharField(max_length = 20, null=False, blank=False)
	student_name = models.CharField(max_length = 200, null=False, blank=False)
	course = models.IntegerField(choices = COURSE_CHOICES, null=False, blank=False)
	picture = models.FileField()
	name_audio = models.ImageField()
