

employees = [{"name": "Aman", "department": "Development", "salary": 45000},
              {"name": "Riya","department": "HR", "salary": 38000},
                {"name": "Neha", "department": "Development", "salary":55000},
                  {"name": "Rahul", "department": "Testing", "salary": 42000},
                    {"name": "Priya", "department":"Development", "salary": 60000}]


# • Use list comprehension to get all employee names.
names = [emp["name"] for emp in employees]
print(names)


# • Get employees earning more than 45,000.
high_salary = [emp for emp in employees
         if emp["salary"] > 45000]
print(high_salary)


# • Get only Development department employees.
dev_employees = [emp for emp in employees
                 if emp["department"] == "Development"]

print(dev_employees)


# • Create a dictionary of employee names and salaries.
name_salary_dict = {
    emp["name"] : emp["salary"]
    for emp in employees
}

print(name_salary_dict)


# • Use map() to calculate yearly salaries.
yearly_salaries = list(map(lambda emp: emp["salary"]*12,employees))
print(yearly_salaries)



# • Use filter() to find employees earning more than 50,000.
high_earners = list(filter(lambda emp: emp["salary"]> 50000, employees))
print(high_earners)



# • Use lambda and sorted() to sort employees by salary.
sorted_employees = sorted(employees, 
                          key=lambda emp: emp["salary"]
                          #,reverse= True
                          )
print(sorted_employees)


# • Group employees by department.
grouped = {}

for emp in employees:
    dept = emp["department"]

    if dept not in grouped:
        grouped[dept] = []

    grouped[dept].append(emp["name"])

print(grouped) 



# • Calculate average salary for each department.
dept_salary = {}

for emp in employees:
    dept = emp["department"]

    if dept not in dept_salary:
        dept_salary[dept] = []
    dept_salary[dept].append(emp["salary"])

for dept, salaries in dept_salary.items():
    average = sum(salaries)/len(salaries)
    print(dept,average)

#print(avg_salary)



# • Find the second-highest distinct salary.
unique_sal = set(emp["salary"] for emp in employees)

sorted_sal = sorted(unique_sal,reverse=True)

second_highest = sorted_sal[1]

print(second_highest)

