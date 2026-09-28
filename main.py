import json

students = []


def load_data():
    try:
        file = open("students.json", "r")
        data = json.load(file)
        file.close()
        return data
    except:
        return []


def save_data():
    file = open("students.json", "w")
    json.dump(students, file, indent=4)
    file.close()


def add_student():

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    try:
        python = float(input("Enter Python marks: "))
        maths = float(input("Enter Maths marks: "))
        english = float(input("Enter English marks: "))
    except:
        print("Please enter marks correctly.")
        return

    if python < 0 or python > 100:
        print("Invalid Python marks.")
        return

    if maths < 0 or maths > 100:
        print("Invalid Maths marks.")
        return

    if english < 0 or english > 100:
        print("Invalid English marks.")
        return

    for s in students:
        if s["roll"] == roll:
            print("Roll number already exists.")
            return

    student = {
        "name": name,
        "roll": roll,
        "python": python,
        "maths": maths,
        "english": english
    }

    students.append(student)
    save_data()

    print("Student added successfully.")


def view_students():

    if len(students) == 0:
        print("No students available.")
        return

    for s in students:

        total = s["python"] + s["maths"] + s["english"]
        average = total / 3

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        print("\nName:", s["name"])
        print("Roll Number:", s["roll"])
        print("Python:", s["python"])
        print("Maths:", s["maths"])
        print("English:", s["english"])
        print("Average:", round(average, 2))
        print("Grade:", grade)
        print("------------------------")


def search_student():

    roll = input("Enter roll number: ")

    for s in students:

        if s["roll"] == roll:

            total = s["python"] + s["maths"] + s["english"]
            average = total / 3

            print("\nStudent found!")
            print("Name:", s["name"])
            print("Roll Number:", s["roll"])
            print("Python:", s["python"])
            print("Maths:", s["maths"])
            print("English:", s["english"])
            print("Average:", round(average, 2))

            return

    print("Student not found.")


def highest_student():

    if len(students) == 0:
        print("No students available.")
        return

    highest = students[0]

    for s in students:

        avg1 = (
            s["python"] +
            s["maths"] +
            s["english"]
        ) / 3

        avg2 = (
            highest["python"] +
            highest["maths"] +
            highest["english"]
        ) / 3

        if avg1 > avg2:
            highest = s

    average = (
        highest["python"] +
        highest["maths"] +
        highest["english"]
    ) / 3

    print("\nHighest Scorer")
    print("Name:", highest["name"])
    print("Roll Number:", highest["roll"])
    print("Average:", round(average, 2))


def update_student():

    roll = input("Enter roll number: ")

    for s in students:

        if s["roll"] == roll:

            try:
                s["python"] = float(input("Enter new Python marks: "))
                s["maths"] = float(input("Enter new Maths marks: "))
                s["english"] = float(input("Enter new English marks: "))
            except:
                print("Invalid marks.")
                return

            save_data()

            print("Student updated.")
            return

    print("Student not found.")


def delete_student():

    roll = input("Enter roll number: ")

    for s in students:

        if s["roll"] == roll:

            students.remove(s)
            save_data()

            print("Student deleted.")
            return

    print("Student not found.")


def main():

    global students

    students = load_data()

    while True:

        print("\n")
        print("===== STUDENT GRADE MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Highest Scorer")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            highest_student()

        elif choice == "5":
            update_student()

        elif choice == "6":
            delete_student()

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Wrong choice. Try again.")


main()
