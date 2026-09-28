def valid_marks(marks):
    return 0 <= marks <= 100


def validate_student(name, roll, python, maths, english):
    errors = []

    if not name.strip():
        errors.append("Student name cannot be empty.")

    if not roll.strip():
        errors.append("Roll number cannot be empty.")

    if not valid_marks(python):
        errors.append("Python marks must be between 0 and 100.")

    if not valid_marks(maths):
        errors.append("Maths marks must be between 0 and 100.")

    if not valid_marks(english):
        errors.append("English marks must be between 0 and 100.")

    return errors
