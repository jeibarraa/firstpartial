https://replit.com/join/oxgbvmlhox-jose-emilioem22
# Grades
grades = []
passed_count = 0
failed_count = 0

#Students
num_students = int(input("Enter the number of students: "))

# Grades
for _ in range(num_students):
    grade = float(input("Enter the student's grade: "))
    grades.append(grade)

    # Check if the student passed or failed
    if grade >= 60:
        passed_count += 1
    else:
        failed_count += 1

# Calculate 
average_grade = sum(grades) / num_students
highest_grade = max(grades)
lowest_grade = min(grades)

# Results
print("\nGrade Statistics:")
print("Average Grade:", average_grade)
print("Highest Grade:", highest_grade)
print("Lowest Grade:", lowest_grade)
print("Number of Students Passed:", passed_count)
print("Number of Students Failed:", failed_count)
