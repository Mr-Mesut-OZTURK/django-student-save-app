from django.shortcuts import get_object_or_404, redirect, render
from .models import Students
from .forms import StudentForm

# Create your views here.


def student_list(request):
    # print(request.path)
    students = Students.objects.all()
    context = {
        "students": students,
    }
    return render(request, "studentlist.html", context)


def student_add(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {
        'form': form,
    }

    return render(request, "studentadd.html", context)


def student_detail(request, id):
    student = Students.objects.get(id=id)
    context = {
        'student': student,
    }
    return render(request, "studentdetail.html", context)


def student_update(request, id):

    student = Students.objects.get(id=id)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {
        'form':form,
        "student":student
    }

    return render(request, "studentupdate.html", context)


def student_delete(request, number):
    student = Students.objects.get(number=number)
    # student=  Students.get_object_or_404(id=id)

    if request.method == "POST":
        student.delete()
        return redirect("list")

    context = {
        'student':student,
    }

    return render(request, "studentdelete.html",context)
