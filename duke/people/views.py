from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import StudentForm
from models import Student

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print form.cleaned_data
            student = Student(**form.cleaned_data)
            # student.student_name = form.cleaned_data['student_name']; 
            student.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()

    return render(request, 'form.html', {'form': form, "header":"form"})

def get_mem(request):
    student_list = Student.objects.filter(course = 1)
    return render(request, 'list.html', {'student_list': student_list, "header":"mem"})


def get_meng(request):
    student_list = Student.objects.filter(course = 2)
    return render(request, 'list.html', {'student_list': student_list, "header":"meng"})