
# Take name, age, email and city from the user and display a formatted introduction.
name = input("Enter your name: ").strip()
while name == "":
    print("Name cannot be empty.")
    name = input("Enter your name: ").strip()

age_text = input("Enter your age: ").strip()
while not age_text.isdigit():
    print("Please enter a valid age (numbers only).")
    age_text = input("Enter your age: ").strip()
age = int(age_text)

email = input("Enter your email: ").strip()
while email == "":
    print("Email cannot be empty.")
    email = input("Enter your email: ").strip()

city = input("Enter your city: ").strip()
while city == "":
    print("City cannot be empty.")
    city = input("Enter your city: ").strip()

print(" User Introduction ")
print(f"Hi, I'm {name}. I'm {age} years old and I live in {city}.")
print(f"You can reach me at {email}.")
print("First Question is complete")


# Build a calculator for addition, subtraction, multiplication, division and modulus.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, %): ")

if operation == "+":
    result = num1+num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

elif operation == "%":
    if num2 != 0:
        result = num1+num2
    else:
        result = "Error! Modulus by zero"

else:
    result = "Invalid operation"

print("Result:", result)
print("Second Question is complete")



# Convert Celsius to Fahrenheit.
celsius = float(input("enter temperature in Celsius: "))

fahrenheit = (celsius*9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")
print("Third Question is complete")


# Calculate rectangle area and perimeter.
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)
print("Fourth Question is complete")


# Calculate a salary after an 18 percent increment.
salary = 450000

increment = salary * 18/100
new_salary = salary + increment 

print("Increment:", increment)
print("New salary:", new_salary)
print("Fifth Question is complete")