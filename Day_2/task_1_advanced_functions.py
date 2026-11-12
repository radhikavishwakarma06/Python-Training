# Create a function that accepts employee details using **kwargs.

def employee_details(**kwargs):
    print("Employee Details:")

    for key, value in kwargs.items():
        print(key,":",value)


employee_details(
    name = "Rahul",
    age = 25,
    department = "IT",
    salary = 45000,
    city = "Indore"
     )


#isinstance() is a built-in Python function that checks the data type of a value.
# isinstance() is useful whenever you want to validate the type of input before performing calculations


def validate_salary(salary: float) -> bool:
    """Check whether salary is a valid positive number."""

    if isinstance(salary, bool):
        return False

    if not isinstance(salary, (int, float)):
        return False

    if salary <= 0:
        return False

    return True

# print(validate_salary(25000))
# print(validate_salary(-500))
# print(validate_salary("abc"))
# print(validate_salary(0))

# • Create a function that accepts any number of salaries using *args and returns total, average, highest
# and lowest salary.
def salary_details(*args: float) -> dict[str,float]:
    """Calculate total, average, highest and lowest salary"""

    if not args:
        print("Error: Please provide at least one salary")
        return {}

    for salary in args:
        if not validate_salary(salary):
            print("Error: Invalid salary value:", salary)
            return {}

    total = sum(args)
    average =  total/len(args)
    highest = max(args)
    lowest = min(args)

    return {
        "Total":total,
        "Average":average,
        "Highest":highest,
        "Lowest":lowest
    }

result = salary_details(20000,50000,44500,30000)
print(result)

print(salary_details())
print(salary_details(20000,-500,30000))
print(salary_details(20000,"abc",30000))

# • Create a closure that maintains a running total.
# nonlocal - It allows the inner function to modify the total variable belonging to the outer function.
#Without nonlocal, Python would not allow us to update that outer variable this way.

def running_total():
    """Create a closure that maintains a running total."""

    total = 0

    def add(amount):
        nonlocal total

        total += amount
        return total

    return add

counter = running_total()

print(counter(100))
print(counter(200))
print(counter(300))


# • Create a decorator named execution_logger that displays the function name, start message, completion
# message and execution time.
# Any -  means arguments and return value can have different data types.
# Callable - A type hint that represents a callable object, such as a function.


import time
from typing import Any

def execution_logger(func):
    """Log function execution details and execution time."""

    def wrapper(*args: Any,**kwargs:Any)-> Any:
        start_time = time.time()

        print("Function:",func.__name__)
        print("Execution started")

        result = func(*args,**kwargs)

        end_time = time.time()

        print("Execution completed")
        print("Execution time:",end_time - start_time)

        return result

    return wrapper


# • Apply the decorator to at least three functions

@execution_logger
def welcome_message():
    """Display aa welcome message"""

    print("Welcome to Advanced Python functions!")


@execution_logger
def add_numbers(a:int, b:int)-> int:
    print(a+b)


@execution_logger
def multiply(a,b):
    print(a*b)


welcome_message()
add_numbers(1,2)
multiply(5,6)

