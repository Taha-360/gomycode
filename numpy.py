import numpy as np

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"

num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

marks_array = np.zeros((num_students, num_subjects))

for i in range(num_students):
    for j in range(num_subjects):
        marks_array[i, j] = float(input(f"Enter marks for student {i+1} and subject {j+1}: "))

# Calculate the total marks for each student
total_marks = np.sum(marks_array, axis=1)

# Calculate the percentage for each student
percentage = (total_marks / (num_subjects * 100)) * 100

# Calculate the grade for each student
grades = np.array([calculate_grade(p) for p in percentage])

# Display the result in a tabular format
print("Student\tTotal Marks\tPercentage\tGrade")
for i in range(num_students):
    print(f"{i+1}\t{total_marks[i]}\t\t{percentage[i]}%\t\t{grades[i]}")
