#!/usr/bin/env python3
"""
Python Loop Examples
This file demonstrates various types of loops in Python
"""

print("=== Python Loop Examples ===\n")

# 1. Basic For Loop
print("1. Basic For Loop:")
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")
print()

# 2. For Loop with List
print("2. For Loop with List:")
fruits = ["apple", "banana", "cherry", "date"]
print("Fruits in the list:")
for fruit in fruits:
    print(f"- {fruit}")
print()

# 3. For Loop with Enumerate
print("3. For Loop with Enumerate (index + value):")
colors = ["red", "green", "blue", "yellow"]
for index, color in enumerate(colors):
    print(f"Color {index + 1}: {color}")
print()

# 4. While Loop
print("4. While Loop:")
print("Countdown from 5:")
countdown = 5
while countdown > 0:
    print(f"T-minus {countdown}")
    countdown -= 1
print("Blast off! 🚀")
print()

# 5. While Loop with User Input Simulation
print("5. While Loop with Condition:")
numbers = [1, 3, 7, 2, 9, 4, 6]
print(f"Finding first number greater than 5 in {numbers}:")
i = 0
while i < len(numbers):
    if numbers[i] > 5:
        print(f"Found: {numbers[i]} at index {i}")
        break
    i += 1
print()

# 6. Nested Loops
print("6. Nested Loops:")
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result:2d}", end="  ")
    print()  # New line after each row
print()

# 7. Loop with Break and Continue
print("7. Loop with Break and Continue:")
print("Processing numbers 1-10, skipping even numbers, stopping at 8:")
for num in range(1, 11):
    if num % 2 == 0:  # Skip even numbers
        continue
    if num >= 8:  # Stop at 8
        print(f"Stopping at {num}")
        break
    print(f"Processing odd number: {num}")
print()

# 8. Dictionary Loop
print("8. Looping through Dictionary:")
student_grades = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "Diana": 88
}
print("Student grades:")
for name, grade in student_grades.items():
    print(f"{name}: {grade}%")
print()

# 9. List Comprehension (Pythonic loop alternative)
print("9. List Comprehension (Alternative to loops):")
squares = [x**2 for x in range(1, 6)]
print(f"Squares of 1-5: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Squares of even numbers 1-10: {even_squares}")
print()

# 10. Infinite Loop with Break (be careful!)
print("10. Controlled Infinite Loop:")
print("Simulating a simple menu system:")
menu_choice = 0
loop_count = 0
while True:
    loop_count += 1
    print(f"Loop iteration {loop_count}")
    
    # Simulate different menu choices
    if loop_count == 1:
        print("User selected: View Profile")
    elif loop_count == 2:
        print("User selected: Settings")
    elif loop_count == 3:
        print("User selected: Exit")
        print("Exiting program...")
        break
    
    if loop_count > 5:  # Safety break
        print("Safety break activated")
        break

print("\n=== End of Loop Examples ===")