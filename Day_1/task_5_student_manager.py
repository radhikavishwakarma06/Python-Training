import json

students = {}

print("Welcome to Student Management System")
print("Student Dictionary:", students)


def get_marks():
    marks = []

    for i in range(1,4):
        while True:
            try:
                mark = int(input(f"Enter marks for subject {i}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break

                else:
                    print("Marks must be between 0 and 100")

            except ValueError:
                print("Please enter a valid number")

    return marks

#print(get_marks())

def add_student():
    name = input("enter student name: ").strip()

    if not name:
        print("Name cannot be empty")
        return
    
    if name.lower() in students:
        print("Student already exists!")
        return

    marks = get_marks()

    students[name.lower()] = {"name": name,
                              "marks": marks}

    print("Student added successfully")
    save_data()
  




def update_marks():
    name = input("enter student name: ").strip().lower()

    if name in students:
        print("Enter updated marks:")
        marks = get_marks()

        students[name]["marks"] = marks

        print("Marks updated successfully!")
        save_data()

    else:
        print("Student not found!")




def update_student_name():
    old_name = input("Enter current student name: ").strip().lower()

    if old_name not in students:
        print("Student not found!")
        return

    new_name = input("Enter new student name: ").strip()

    if not new_name:
        print("Name cannot be empty!")
        return

    if new_name.lower() in students:
        print("Student name already exists!")
        return

    students[new_name.lower()] = students.pop(old_name)
    students[new_name.lower()]["name"] = new_name

    print("Student name updated successfully!")
    save_data()


def delete_student():
    name = input("Enter student name to delete: ").strip().lower()

    if name in students:
        students.pop(name)
        print("Student deleted successfully!")
        save_data()

    else:
        print("Student not found!")


def view_students():
    if not students:
        print("No students found!")
        return

    for key, details in students.items():
        print("\nStudent Name:", details["name"])
        print("Marks:", details["marks"])

# add_student()
# view_students()

def search_student():
    name = input("Enter student name to search: ").strip().lower()

    if name in students:
        details = students[name]

        print("Student Found!")
        print("Name:", details["name"])
        print("Marks:", details["marks"])

    else:
        print("Student not found!")

# add_student()
# search_student()

def calculate_result():
    name = input("Enter student name: ").strip().lower()

    if name in students:
        marks = students[name]["marks"]

        total = sum(marks)
        average = total / len(marks)

        print("Student Name:", students[name]["name"])
        print("Total Marks:", total)
        print("Average Marks:", average)

    else:
        print("Student not found!")

# add_student()
# calculate_result()


def display_result():
    name = input("Enter student name: ").strip().lower()

    if name in students:
        marks = students[name]["marks"]

        if all(mark >= 40 for mark in marks):
            print("Result: PASS")
        else:
            print("Result: FAIL")

    else:
        print("Student not found!")

# add_student()
# display_result()

def highest_student():
    if not students:
        print("No students found!")
        return

    highest_name = None
    highest_total = -1

    for key, details in students.items():
        total = sum(details["marks"])

        if total > highest_total:
            highest_total = total
            highest_name = key

    print("Highest Scoring Student:", students[highest_name]["name"])
    print("Total Marks:", highest_total)

# add_student()
# add_student()
# highest_student()

def main_menu():
    while True:
        print("\n STUDENT MANAGEMENT SYSTEM ")
        print("1. Add Student")
        print("2. Update Student Marks")
        print("3. Update Student Name")
        print("4. Delete Student")
        print("5. View All Students")
        print("6. Search Student")
        print("7. Calculate Total and Average")
        print("8. Display Pass/Fail")
        print("9. Highest Scoring Student")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            update_marks()

        elif choice == "3":
            update_student_name()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            view_students()

        elif choice == "6":
            search_student()

        elif choice == "7":
            calculate_result()

        elif choice == "8":
            display_result()

        elif choice == "9":
            highest_student()

        elif choice == "10":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice! Please select 1 to 10.")



def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Student data saved successfully!")


def load_data():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

        print("Student data loaded successfully!")

    except FileNotFoundError:
        students = {}
        print("No previous student data found!")

# This handles invalid JSON content, such as an empty file or incorrectly formatted JSON.
    except json.JSONDecodeError:
        students = {}
        print("JSON file is empty or corrupted. Starting with empty data")


load_data()
main_menu()
save_data()