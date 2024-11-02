"""
Exercise 18 - Multiple Inheritance
https://github.com/codebasics/py/tree/master/Basics/Exercise
"""


# 1. Create multiple inheritance on teacher,student and youtuber.
# Q. if we have created teacher and now one student joins master degree
# with becoming teacher then what?
#
# Ans : just make subclass from teacher
# so that student will become a teacher
#
# 2. Now student is teacher as well as youtuber then what?
# Ans : just use multiple inheritance for these three relations


class Teacher:
    """Represents a teacher with specific skills."""

    @staticmethod
    def teacher_skills() -> None:
        """Display the skills of a teacher."""
        print("\tI have a master's degree & I can teach")


class Student:
    """Represents a student with specific skills."""

    @staticmethod
    def student_skills() -> None:
        """Display the skills of a student."""
        print("\tI am still learning")


class Youtuber:
    """Represents a YouTuber with specific skills."""

    @staticmethod
    def youtuber_skills() -> None:
        """Display the skills of a YouTuber."""
        print("\tI upload videos")


class Person(Teacher, Student, Youtuber):
    """Represents a person who inherits skills from Teacher, Student, and Youtuber."""

    @staticmethod
    def display_skills() -> None:
        """Display all skills from Teacher, Student, and YouTuber."""
        Teacher.teacher_skills()
        Student.student_skills()
        Youtuber.youtuber_skills()


def main() -> None:
    """Create a student instance and display information"""
    student = Person()
    student.display_skills()


if __name__ == "__main__":
    print(__doc__)
    main()
