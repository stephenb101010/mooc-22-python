class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list):
    attempts = filter(lambda attempt: attempt.grade >= 1, attempts)
    return list(attempts)

def attempts_with_grade(attempts: list, grade: int):
    attempts = filter(lambda attempt: attempt.grade == grade, attempts)
    return list(attempts)

def passed_students(attempts: list, course: str):
    attempts = filter(lambda attempt: attempt.course_name == course and attempt.grade > 0, attempts)
    attempts = map(lambda attempt: attempt.student_name, attempts)
    attempts = list(attempts)
    attempts.sort()
    return attempts

"""
def accepted(attempts: list):
    return filter(lambda s: s.grade>0, attempts)

def attempts_with_grade(attempts: list, grade: int):
    return filter(lambda s: s.grade==grade, attempts)

def passed_students(attempts: list, course: str):
    course_attempts = filter(lambda s: s.course_name==course and s.grade>0, attempts)
    course_students = map(lambda s: s.student_name, course_attempts)
    return sorted(course_students)
"""