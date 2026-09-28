from grades import calculate_average, get_grade


def highest_scorer(students):
    if len(students) == 0:
        print("No students found.")
        return

    highest = students[0]

    for student in students:
        if calculate_average(student) > calculate_average(highest):
            highest = student

    average = calculate_average(highest)

    print("\n===== HIGHEST SCORER =====")
    print("Name:", highest["name"])
    print("Roll Number:", highest["roll"])
    print("Average:", round(average, 2))
    print("Grade:", get_grade(average))
