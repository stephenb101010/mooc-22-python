class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def names_of_students(attempts: list):
    names = map(lambda attempt: attempt.student_name, attempts)
    return list(names)

def course_names(attempts: list):
    def get_course(attempt: CourseAttempt):
        return attempt.course_name
    courses = map(get_course, attempts)
    courses = list(set(list(courses)))
    courses.sort()
    return courses

"""
def names_of_students(course_names: list):
    def student(attempt: CourseAttempt):
        return attempt.student_name
    return map(student, course_names)
    # same using lambda function
    # return map(lambda k: k.student_name, course_names)

def course_names(course_names: list):
    names = map(lambda k: k.course_name, course_names)
    # remove duplicates by using a set
    return sorted(list(set(names)))
"""