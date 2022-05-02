from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Pesho", {"Python": ["advanced"]})

    def test_is_instance_set(self):
        self.assertEqual("Pesho", self.student.name)
        self.assertEqual({'Python': ['advanced']}, self.student.courses)

    def test_leave_course_when_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("JS")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_when_course_is_found(self):
        result = self.student.leave_course("Python")
        self.assertEqual("Course has been removed", result)

    def test_add_notes_when_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("JS", "advanced")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_when_course_is_found(self):
        result = self.student.add_notes("Python", "OOP")
        self.assertEqual("Notes have been updated", result)

    def test_enroll_when_course_name_is_not_in_courses_and_should_not_add_notes(self):
        result = self.student.enroll("JS", "advanced", "N")
        self.assertEqual([], self.student.courses["JS"])
        self.assertEqual("Course has been added.", result)

    def test_enroll_when_course_name_is_not_in_courses_and_should_add_notes(self):
        result = self.student.enroll("JS", "advanced", "Y")
        self.assertEqual("advanced", self.student.courses["JS"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_when_course_name_is_not_in_courses_and_should_add_notes_without_yes_param(self):
        result = self.student.enroll("JS", "advanced", "")
        self.assertEqual("advanced", self.student.courses["JS"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enrol_when_course_name_is_in_courses(self):
        result = self.student.enroll("Python", ["basic", "OOP"], "")
        self.assertEqual(['advanced', 'basic', 'OOP'], self.student.courses["Python"])
        self.assertEqual("Course already added. Notes have been updated.", result)


if __name__ == "__main__":
    main()
