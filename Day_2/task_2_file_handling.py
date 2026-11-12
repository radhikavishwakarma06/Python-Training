import json
import os
FILE_NAME = "employees.json"


def load_employees():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Employee file not found. Starting with empty records.")
        return []

    except json.JSONDecodeError:
        print("Error: Invalid JSON data in employees.json")
        return None



# employees = load_employees()
# print(employees)
# dump() means write Python data into a JSON file.
# indent controls the formatting and spacing of JSON data.


def save_employees(employees):
    with open(FILE_NAME,"w") as file:
        json.dump(employees, file, indent=4)

    print("Employee data saved successfully")

def find_employee(employees,emp_id: int):
    for employee in employees:
        if employee["id"] == emp_id:
            return employee
    return None

def validate_salary(salary:float)-> float | None:
    try:
        salary = float(salary)

        if salary < 0:
            print("Salary cannot be negative!")
            return None

        return salary

    except (ValueError,TypeError):
        print("Invalid salary! Please enter a numeric value.")
        return None


def add_employee(emp_id: int, name:str, email: str,
                 department:str,salary:float)-> None:
    employees = load_employees()

    if employees is None:
        return

    if find_employee(employees,emp_id):
        print(f"Employee ID '{emp_id}' already exists")
        return

    salary = validate_salary(salary)

    if salary is None:
        return

    employees.append({
        "id":emp_id,
        "name": name,
        "email":email,
        "department": department,
        "salary":salary,
    })

    save_employees(employees)
    print(f"Employee '{name}' added successfully.")


def display_all_employees():
    employees = load_employees()

    if employees is None:
        return

    if not employees:
        print("No employee found")
        return

    for emp in employees:
        print(f"ID: {emp['id']} | Name: {emp['name']} | Email: {emp['email']} "
              f"| Dept: {emp['department']} | Salary: {emp['salary']}")

add_employee(
    101,
    "Rahul",
    "rahul@gmail.com",
    "IT",
    30000
)      

#display_all_employees()

def search_employee(emp_id:int):
    employee = find_employee(load_employees(),emp_id)


    if employee:
        print(f"Found: '{employee}'")
    else:
        print(f"Employee ID '{emp_id}' not found.")

#search_employee(101)

def update_employee(emp_id: int, new_department = None,new_salary = None):
    employees = load_employees()

    if employees is None:
        return

    employee = find_employee(employees,emp_id)

    if not employee:
        print("employee not found")
        return

    if new_department is not None:
        employee["department"] = new_department

    if new_salary is not None:
        salary = validate_salary(new_salary)

        if salary is None:
            return
        
        employee["salary"] = salary

    if new_department is None and new_salary is None:
        print("Please provide department or salary to update!")
        return

    save_employees(employees)
    print("Employee details updated successfully!")



#update_employee(101, "Data Science",45000)
#display_all_employees()


def delete_employee(emp_id: int):
    employees = load_employees()

    if employees is None:
        return

    employee = find_employee(employees, emp_id)

    if employee:
        employees.remove(employee)

        save_employees(employees)

        print(f"Employee ID {emp_id} deleted successfully!")

    else:
        print("Employee not found!")

# delete_employee(101)
# display_all_employees()

def count_employees():
    employees = load_employees()

    if employees is None:
        return

    total = len(employees)

    print(f"Total Employees: {total}")

#count_employees()

def get_employee_id():
    try:
        emp_id = int(input("Enter Employee ID: "))
        return emp_id

    except ValueError:
        print("Invalid ID! Please enter a number.")
        return None


def menu():
    while True:
        print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Count Employees")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            emp_id = get_employee_id()

            if emp_id is None:
                continue

            name = input("Enter Name: ").strip()
            email = input("Enter Email: ").strip()
            department = input("Enter Department: ").strip()
            salary = input("Enter Salary: ").strip()

            if not name or not email or not department:
                print("All employee details are required!")
                continue

            add_employee(emp_id, name, email, department, salary)

        elif choice == "2":
            display_all_employees()

        elif choice == "3":
            emp_id = get_employee_id()

            if emp_id is not None:
                search_employee(emp_id)

        elif choice == "4":
            emp_id = get_employee_id()

            if emp_id is None:
                continue

            print("\n1. Update Department")
            print("2. Update Salary")
            print("3. Update Both")

            update_choice = input("Enter your choice: ").strip()

            if update_choice == "1":
                department = input("Enter New Department: ").strip()
                update_employee(emp_id, new_department=department)

            elif update_choice == "2":
                salary = input("Enter New Salary: ").strip()
                update_employee(emp_id, new_salary=salary)

            elif update_choice == "3":
                department = input("Enter New Department: ").strip()
                salary = input("Enter New Salary: ").strip()

                update_employee(
                    emp_id,
                    new_department=department,
                    new_salary=salary
                )

            else:
                print("Invalid update choice!")

        elif choice == "5":
            emp_id = get_employee_id()

            if emp_id is not None:
                delete_employee(emp_id)

        elif choice == "6":
            count_employees()

        elif choice == "7":
            print("Thank you for using Employee Management System!")
            break

        else:
            print("Invalid choice! Please select 1 to 7.")


if __name__ == "__main__":
    menu()