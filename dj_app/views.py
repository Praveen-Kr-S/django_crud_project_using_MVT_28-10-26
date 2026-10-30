from django.shortcuts import render
from .forms import StudentForm
from .models import StudentData

def AllStudents(request):
    context = {
        'name':'Vinoth',
        'dept':'mech',
        'phone':'7418529635'
    }
    return render(request,"allstudents.html",context)


def AddStudent(request):#post
    add_form = StudentForm()

    if request.method == "POST":
        print(request.POST)
        add_form = StudentForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            
    return render(request, "addstudent.html",{'add_form':add_form})