# Empty lists for student names, marks, and pass status
student_names = []
marks = []
has_passed = []

# Example data
student_names.append("Alice")
marks.append(85)

student_names.append("Bob")
marks.append(45)

student_names.append("Charlie")
marks.append(75)

student_names.append("David")
marks.append(55)

# Determine if each student has passed
passing_mark = 50  # Define the passing mark

for mark in marks:
    if mark >= passing_mark:
        has_passed.append(True)
    else:
        has_passed.append(False)

# Combine the lists into a nested list
results = []

for i in range(len(student_names)):
    results.append([student_names[i], marks[i], has_passed[i]])

# Print the results
for result in results:
    print(result)