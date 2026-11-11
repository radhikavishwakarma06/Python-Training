# Find the largest and smallest list values.
numbers = [10, 25, 5, 40, 15, 2]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)


# • Find the second-largest distinct number without sorting the complete list.
numbers = [10, 25, 40, 25, 15, 40, 30]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:

    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number:", second_largest)


# • Remove duplicates while preserving order.
numbers = [10, 20, 10, 30, 20, 40, 50, 30]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:", unique)

# • Separate even and odd numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)


# • Find common values between two lists.
a = [10, 20, 30, 40, 50]
b = [30, 40, 50, 60, 70]

common = []

for num in a:
    if num in b and num not in common:
        common.append(num)

print("Common values:", common)


# • Count frequency of each number.

numbers = [1,2,2,3,1,2]
freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)


# • Create a marks dictionary and find the highest scorer, lowest scorer and average.

marks = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 75,
    "Neha": 88,
    "Rohit": 65
}

highest = max(marks, key=marks.get)
lowest = min(marks, key=marks.get)

total = 0

for score in marks.values():
    total += score

average = total / len(marks)

print("Highest Scorer:", highest)
print("Highest Marks:", marks[highest])

print("Lowest Scorer:", lowest)
print("Lowest Marks:", marks[lowest])

print("Average Marks:", average)