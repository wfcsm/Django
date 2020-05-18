from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Grades, Students


def index(request):
    return HttpResponse("11")


def detail(request, num, num2):
    return HttpResponse("derail-%s-%s" % (num, num2))


def grades(request):
    gradesList = Grades.objects.all()
    return render(request, 'myApp/grades.html', {'grades': gradesList})


def student(request):
    studentList = Students.objects.all()
    return render(request, 'myApp/students.html', {'students': studentList})


def grades_students(request, num):
    grade = Grades.objects.get(pk=num)
    print(1)
    studentList = grade.students_set.all()
    return render(request, 'myApp/students.html', {'students': studentList})