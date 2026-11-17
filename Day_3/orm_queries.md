1. Get all students.

from students.models import Student, Department, StudentProfile, Course
Student.objects.all()
<QuerySet [<Student: Rahul>, <Student: Parul>, <Student: suraj>, <Student: aayush>, <Student: ansh>, <Student: priya>, <Student: Neha>, <Student: Rohit>, <Student: karan>, <Student: Sneha>]>

2. Get only active students.
Students.objects.filter(is_active = True)
<QuerySet [<Student: Rahul>, <Student: Parul>, <Student: suraj>, <Student: aayush>, <Student: ansh>, <Student: Neha>, <Student: Rohit>, <Student: karan>, <Student: Sneha>]>

3. Get students whose marks are greater than or equal to 60.
Students.objects.filters(marks__gte = 60)
<QuerySet [<Student: Rahul>, <Student: Parul>, <Student: suraj>, <Student: ansh>, <Student: priya>, <Student: karan>, <Student: Sneha>]>

4. Get students whose names contain a given word.
Student.objects.filter(name__icontains="rah")
<QuerySet [<Student: Rahul>]>

5. Order students by marks.
Student.objects.order_by("marks")
<QuerySet [<Student: aayush>, <Student: Neha>, <Student: Rohit>, <Student: Parul>, <Student: suraj>, <Student: karan>, <Student: Rahul>, <Student: priya>, <Student: ansh>, <Student: Sneha>]>

6. Get the top three students by marks.
Student.objects.order_by('-marks')[:3]
<QuerySet [<Student: Sneha>, <Student: ansh>, <Student: priya>]>

7. Get students from a specific department.
Student.objects.filter(department__name = "Data Science")
<QuerySet [<Student: aayush>, <Student: ansh>, <Student: Neha>]>

8. Get students enrolled in a specific course.
Student.objects.filter(course__name = "Django")
<QuerySet [<Student: Neha>]>

9. Get all courses for one student.
Student.objects.get(id=1)
<QuerySet <Student: Rahul>
student = Student.objects.get(id=1)
student = Student.objects.get(id=3)
student.courses.all()
<QuerySet [<Course: Django - DJ102>, <Course: Python - PY101>]>

from django.db.models import Avg,Max,Min,Count,Q

10. Count the total number of students.
    Student.objects.count()
    10

11. Calculate average marks.
    Student.objects.aggregate(avarage_marks = Avg("marks"))
Out[9]: {'avarage_marks': 70.3}

12. Find the highest and lowest marks.
     Student.objects.aggregate(highest_marks=Max("marks"),lowest_marks=Min("marks"))
Out[10]: {'highest_marks': 93.0, 'lowest_marks': 45.0}


13. Count students in each department.
    Query : for dept in Department.objects.annotate(total_student=Count("students")): print(dept.name, dept.total_student)

    Computer Science 4
    Data Science 3
    Information Technology 3


14. Find departments with more than three students.
In [19]: Department.objects.annotate(total_student=Count("students")).filter(total_student__gt = 3)
Out[19]: <QuerySet [<Department: Computer Science>]>
    
15. Find students who do not have a profile.
    Student.objects.filter(profile__isnull=True)
    Out[20]: <QuerySet [<Student: priya>, <Student: Neha>, <Student: Rohit>, <Student: karan>, <Student: Sneha>]>

16. Find students enrolled in more than one course.
    Student.objects.annotate(total_courses=Count('courses',distinct=True)).filte
        ...: r(total_courses__gt = 1)
    Out[22]: <QuerySet [<Student: suraj>, <Student: Parul>]>

17. Search students by name or email using Q objects.
: Student.objects.filter(
        Q(name__icontains="neha") |
       Q(email__icontains="neha")
     )
 <QuerySet [<Student: Neha>, <Student: Sneha>]>

18. Update inactive students to active using update().
    Student.objects.filter(is_active = False).update(is_active=True)
    Out[25]: 1

19. Delete records with invalid marks, if any.
    invalid_students = Student.objects.filter(
             Q(marks__lt=0) | Q(marks__gt=100)
         )

    invalid_students.delete()
    (0, {})


20. Use select_related() and prefetch_related() appropriately
    students = Student.objects.select_related(
        'department',
        'profile'
    ).prefetch_related('courses')

    for student in students:
        print("Name:", student.name)
        print("Department:", student.department)
        print("Profile:", student.profile)
        print("Courses:", list(student.courses.all()))

## outpName: Rahul
Department: Computer Science
Profile: Rahul - Profile
Courses: [<Course: Machine Learning - ML104>]
Name: Parul
Department: Information Technology
Profile: Parul - Profile
Courses: [<Course: Data Analytics - Da105>, <Course: DBMS - DB103>]
Name: suraj
Department: Computer Science
Profile: suraj - Profile
Courses: [<Course: Django - DJ102>, <Course: Python - PY101>]
Name: aayush
Department: Data Science
Profile: aayush - Profile
Courses: []
Name: ansh
Department: Data Science
Profile: ansh - Profile
Courses: []
Name: priya
Department: Computer Science
Profile: No profile available
Courses: []

