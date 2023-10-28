def _init_(self, name, roll_number, cgpa):
  self.name = name
  self.roll_number = roll_number
  self.cgpa = cgpa

def sort_students(student_list):
# Sort the student list based on CGPA in descending order
sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
return sorted_students

# Example usage:

# Create a list of student objects
students = [
Student("Alice", "101", 3.9),
Student("Bob", "102", 3.7),
Student("Charlie", "103", 4.0),
Student("David", "104", 3.8),
]

# Sort the list of students by CGPA
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")