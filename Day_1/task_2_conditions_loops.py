

# Check positive, negative or zero.
def check_number():
    number = float(input("Enter a number : "))

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("zero")

check_number()

# Check even or odd
def check(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

check(5)


# Find the largest of three numbers.

def larget_number():
    a = 25   #20
    b = 40   #20
    c = 15


    if a >= b and a>=c:
        print(a)
    elif b >= a and b>=c:
        print(b)
    else:
        print(c)

larget_number()


# Print a multiplication table.
n = int(input("enter number : "))
for i in range(1,11): 
    print(n, "x", i,"=", n*i)
    

# Calculate the sum from 1 to n.
n = int(input("Enter a number: "))

total = 0
i = 1

while i <= n:
    total = total + i
    i += 1

print("Sum from 1 to", n, "is:", total)


# Check whether a number is prime.
n = 5

if n <= 1:
    print("not a prime")

else:
    for i in range(2,(int(n**0.5)+1)):
        if n%1 == 0:
            print("not a prime")
            break

    else:
        print("Prime No.")


# print even numbers from 1 to 100
for i in range(1,101):
    if i%2 == 0:
        print(i)