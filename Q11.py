students = {
    "Aman": 85,
    "Riya": 92,
    "John": 78,
    "Sara": 88,
    "Neha": 95
}

# Topper
topper = max(students, key=students.get)
print("Topper:", topper)

# Average
avg = sum(students.values()) / len(students)
print("Average Marks:", avg)
