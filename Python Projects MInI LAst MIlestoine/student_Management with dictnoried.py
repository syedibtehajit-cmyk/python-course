students = []

number_of_students = int(input("How many students do you want to add? "))

for i in range(number_of_students):

    print("\nEnter Student", i + 1, "Details")
    print("----------------")

    student_name = input("Enter your Name: ")

    math_marks = int(input("Enter Math Marks: "))
    english_marks = int(input("Enter English Marks: "))
    science_marks = int(input("Enter Science Marks: "))

    # Calculate Total
    total = math_marks + english_marks + science_marks

    # Calculate Average
    average = total / 3

    # Calculate Percentage
    percentage = (total / 300) * 100

    # Calculate Grade
    if percentage >= 80:
        grade = "A1"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    # Calculate Pass / Fail
    if math_marks >= 40 and english_marks >= 40 and science_marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    # Student Dictionary
    student = {
        "name": student_name,
        "math": math_marks,
        "english": english_marks,
        "science": science_marks,
        "total": total,
        "average": average,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }

    # Add student to list
    students.append(student)

    # Display Result
    print("\nStudent Name:", student["name"])
    print("----------------")
    print("English Marks:", student["english"])
    print("----------------")
    print("Science Marks:", student["science"])
    print("----------------")
    print("Math Marks:", student["math"])
    print("----------------")
    print("Total Marks:", student["total"])
    print("----------------")
    print("Average:", student["average"])
    print("----------------")
    print("Percentage:", student["percentage"])
    print("----------------")
    print("Grade:", student["grade"])
    print("----------------")
    print("Result:", student["result"])
    print("================")


print("\nAll Students:")
print(students)