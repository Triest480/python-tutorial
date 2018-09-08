#!/usr/bin/env python3

# This is gonna be up to you. But basically I envisioned a system where you have a students in a classroom. Where the
# classroom only has information, like who is the teacher, how many students are there. And it's like an online class,
# so students don't know who their peers are, or who their teacher is, but can do things like study, and take test and
# stuff. Etc. But get used to how objects interact with each other and try to call stuff from other places while being
# commanded all in main():


class Student:
    def __init__(self, name, laziness=5):
        self.name = name
        self.preparedness = 0
        self._laziness = laziness

    def takeTest(self, hardness):
        # TODO: return a score that's 100 - difference between hardness and preparedness (score capped at 100)
        return 0

    def doHomework(self):
        # TODO: return a score of either 0 or 100 depending on how lazy they are. Implementation is up to you.
        return 0

    def study(self):
        # TODO: increment preparedness by a random number between 1-10 (prerparedness capped at 100)
        pass


class Teacher:
    def __init__(self, name):
        self.name = name
        self.classroom = None
        self.test_grades = {}
        self.homework_grades = {}

    def administerTest(self, students, hardness):
        # TODO: Given a hardness of a test and list of students. Make each student take test and log their grades
        pass

    def giveHomework(self, students):
        # TODO: Given homework to student and log in their grades
        pass

    def giveGrades(self, students):
        # TODO: Given all the test scores and homework score in each student, give 30% to HW and 70% to test.
        # TODO: Return list of passed students and remove them from classroom. Clear grades for all remaining students
        pass


class ClassRoom:
    def __init__(self):
        self.class_size_limit = 10
        self.students = {}
        self.teacher = None

    def addStudent(self, student):
        # TODO: add student to class. Print something if they try to add the same student or go over the limit
        pass

    def assignTeacherToClass(self, teacher):
        # TODO: Assign teacher, also prompt user if they want to switch teacher if one already assigned or same teacher
        pass

    def getStudents(self):
        # TODO: return a list of students
        return


if __name__ == '__main__':
    classroom = ClassRoom()
    teacher = Teacher('Doctor Jones')
    mike = Student('Mike')
    sally = Student('Sally', laziness=1)
    lebron = Student('Lebron', laziness=10)

    # TODO: Assign a teacher to the classroom and add the students to the classroom. Then make the students study
    # TODO: Make Students to homework, etc, exams, then pass or fail them, etc. Play around with it.
