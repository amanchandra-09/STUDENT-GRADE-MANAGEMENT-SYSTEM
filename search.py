from grades import calculate_average, get_grade


def search_student(students):
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:

            average = calculate_average(student)
            grade = get_grade(average)

            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll"])
            print("Python:", student["python"])
            print("Maths:", student["maths"])
            print("English:", student["english"])
            print("Average:", round(average, 2))
            print("Grade:", grade)

            return

    print("Student not found.")
