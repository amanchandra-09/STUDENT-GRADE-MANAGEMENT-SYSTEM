import unittest

from grades import calculate_average, get_grade
from validation import validate_student


class TestStudentGradeSystem(unittest.TestCase):

    def test_average(self):
        student = {
            "name": "Rahul",
            "roll": "101",
            "python": 80,
            "maths": 90,
            "english": 70
        }

        self.assertEqual(calculate_average(student), 80)

    def test_grade_a_plus(self):
        self.assertEqual(get_grade(95), "A+")

    def test_grade_a(self):
        self.assertEqual(get_grade(85), "A")

    def test_grade_b(self):
        self.assertEqual(get_grade(75), "B")

    def test_invalid_marks(self):
        errors = validate_student(
            "Rahul",
            "101",
            110,
            80,
            90
        )

        self.assertTrue(len(errors) > 0)

    def test_empty_name(self):
        errors = validate_student(
            "",
            "101",
            80,
            80,
            80
        )

        self.assertTrue(len(errors) > 0)


if __name__ == "__main__":
    unittest.main()
