from storage import load_students, save_students
from validation import validate_student


def add_student(students):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    try:
        python = float(input("Enter Python marks: "))
        maths = float(input("Enter Maths marks: "))
        english = float(input("Enter English marks: "))
    except ValueError:
        print("Please enter valid numbers for marks.")
        return

    errors = validate_student(
        name,
        roll,
        python,
        maths,
        english
    )

    if errors:
        for error in errors:
            print("Error:", error)
        return

    if any(student["roll"] == roll for student in students):
        print("A student with this roll number already exists.")
        return

    student = {
        "name": name.strip(),
        "roll": roll.strip(),
        "python": python,
        "maths": maths,
        "english": english
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def view_students(students):
    if len(students) == 0:
        print("No students found.")
        return

    print("\n===== STUDENT DETAILS =====")

    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll"])
        print("Python:", student["python"])
        print("Maths:", student["maths"])
        print("English:", student["english"])
        print("---------------------------")


def update_student(students):
    roll = input("Enter roll no to update: ")

    for student in students:
        if student["roll"] == roll:

            try:
                python = float(
                    input("Enter new Python marks: ")
                )
                maths = float(
                    input("Enter new Maths marks: ")
                )
                english = float(
                    input("Enter new English marks: ")
                )
            except ValueError:
                print("Please enter valid marks.")
                return

            errors = validate_student(
                student["name"],
                student["roll"],
                python,
                maths,
                english
            )

            if errors:
                for error in errors:
                    print("Error:", error)
                return

            student["python"] = python
            student["maths"] = maths
            student["english"] = english

            save_students(students)

            print("Student details updated successfully!")
            return

    print("Student not found.")


def delete_student(students):
    roll = input("Enter roll no to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students(students)

            print("Student deleted successfully!")
            return

    print("Student not found.")
