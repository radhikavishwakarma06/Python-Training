from django.shortcuts import render, redirect,get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages


def student_list(request):
    students = Student.objects.all()
    total_students = Student.objects.count()
    active_students = Student.objects.filter(
        is_active = True
    ).count()

    context = {
        'students': students,
        'total_students': total_students,
        "active_students": active_students,
    }

    return render(request, "students/student_list.html",context)


def add_student(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully")
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(request, 'students/add_student.html',{'form': form})

def home(request):
    return render(request, 'students/home.html')

def about(request):
    return render(request,'students/about.html')

def edit_student(request, id):
    student = get_object_or_404(Student,id=id)

    if request.method == "POST":
        form = StudentForm(request.POST,instance = student)

        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully")
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    return render(request, "students/edit_student.html", {"form": form})

def delete_student(request, id):
    student = get_object_or_404(Student,id = id)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully")
        return redirect('student_list')

    return render(
        request,
        'students/delete_student.html',
        {'student':student}

    )