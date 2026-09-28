from storage import load_students
from students import (
    add_student,
    view_students,
    update_student,
    delete_student
)
from search import search_student
from reports import highest_scorer
from ui import show_menu


students = load_students()


while True:

    choice = show_menu()

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        highest_scorer(students)

    elif choice == "5":
        update_student(students)

    elif choice == "6":
        delete_student(students)

    elif choice == "7":
        print(
            "Thank you for using "
            "STUDENT GRADE MANAGEMENT SYSTEM"
        )
        break

    else:
        print("Invalid choice. Please try again.")
