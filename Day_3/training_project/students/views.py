from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import Student,Department,Course
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db.models import Avg,Count,Q


def home(request):
    return render(request, 'students/home.html')


@login_required
def dashboard(request):
    total_students = Student.objects.count()

    active_students = Student.objects.filter(
        is_active = True).count()
    total_departments = Department.objects.count()
    total_courses = Course.objects.count()
    average_marks = Student.objects.aggregate(
        average = Avg('marks')
    )
    highest_student = Student.objects.order_by('-marks').first()
    recent_students = Student.objects.order_by('-joined_date')[:5]

    context = {
        'total_students': total_students,
        'active_students': active_students,
        'total_departments': total_departments,
        'total_courses': total_courses,
        'average_marks' : average_marks['average'],
        'highest_students':highest_student,
        'recent_students': recent_students,
        
    }
    return render(request, 'students/dashboard.html',context)


@login_required
def student_list(request):
    print("User:", request.user)
    print("Authenticated:", request.user.is_authenticated)
    students = Student.objects.annotate(
        total_courses = Count('courses',distinct=True)
    )

    department_id = request.GET.get('department')
    if department_id:
        students = students.filter(department_id=department_id)

    course_id = request.GET.get('course')
    if course_id:
        students = students.filter(courses__id = course_id)

    status = request.GET.get('status')

    if status == "active":
        students = students.filter(is_active= True)

    elif status == "inactive":
        students = students.filter(is_active=False)

    result = request.GET.get('result')

    if result == 'pass':
        students = students.filter(marks__gte=40)

    elif result == 'fail':
        students = students.filter(marks__lt = 40)

    search_query = request.GET.get('search')

    if search_query:
        students = students.filter(
            Q(name__icontains = search_query) |
            Q(email__icontains = search_query) |
            Q(courses__course_name__icontains = search_query)
        ).distinct()



    total_students = Student.objects.count()
    active_students = Student.objects.filter(
        is_active = True
    ).count()


    context = {
        'students': students,
        'total_students': total_students,
        "active_students": active_students,
        'departments': Department.objects.all(),
        'courses': Course.objects.all(),
    }

    return render(request, "students/student_list.html",context)


@login_required
def add_student(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully")
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(request, 'students/student_form.html',{'form': form,
                     'title':"Add Student",'button_text': 'Add Student'})


@login_required
def student_detail(request,id):
    student = get_object_or_404(Student,id=id)

    return render(
        request, 'students/student_detail.html',
        {'student': student}
    )

@login_required
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

    return render(request, "students/student_form.html",
                   {"form": form,'title': 'Edit Student',"button_text": "Edit Student"})


def is_staff_user(user):
    return user.is_staff


@login_required
@user_passes_test(is_staff_user)
def delete_student(request, id):
    student = get_object_or_404(Student,id = id)


    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully")
        return redirect('student_list')

    return render(
        request,
        'students/student_confirm_delete.html',
        {'student':student}

    )

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Student Registered successfully"
                             )
            return redirect("login")
        
        # else:
        #     messages.error(request, "Please correct the errors above.")
    else:
        form = UserCreationForm()

    return render(request,'students/register.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)

            #messages.success(request,"Student Loggedin successfully"  )
            return redirect("student_list")

        else:
            messages.error(request, "Invalid username or password")

    return render(request,'students/login.html')


def user_logout(request):
    logout(request)
    #messages.success(request,"You have been logged out successfully!")
    return redirect("login")