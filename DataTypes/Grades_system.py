grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Fay": 90,
    "Grace": 77,
    "Hank": 95
}

# Print the grade of alice
print("Alice's grade is:", grades["Alice"])

# Add new student Eve with a grade of 88

grades["Eve"] = 88

# Upgrade the grade of Bob to 95
grades["Bob"] = 95

# Remove charlie from the system
del grades["Charlie"]

# Print each student and their grade

for name, grade in grades.items():
    print(f'student {name} has a grade of {grade}')

# Check if david is in the system
if "David" in grades:
    print('David is still in the system')
else:
    print("David is not in the system")