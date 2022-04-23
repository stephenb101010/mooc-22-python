from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(attempts: list):
    sum = reduce(lambda credits_sum, attempt: credits_sum + attempt.credits, attempts, 0)
    return sum

def sum_of_passed_credits(attempts: list):
    attempts = filter(lambda attempt: attempt.grade >= 1, attempts)
    sum = reduce(lambda credits_sum, attempt: credits_sum + attempt.credits, attempts, 0)
    return sum

def average(attempts: list):
    attempts = filter(lambda attempt: attempt.grade >= 1, attempts)
    attempts = list(attempts)
    sum = reduce(lambda grade_sum, attempt: grade_sum + attempt.grade, attempts, 0)
    return round(sum/len(attempts), 2)

"""
def credit_summer(cr_sum, attempt):
    return cr_sum + attempt.credits

def sum_of_all_credits(attempts: list):
    return reduce(credit_summer, attempts, 0)

def sum_of_passed_credits(attempts: list):
    accepted = filter(lambda s: s.grade > 0, attempts)
    return reduce(credit_summer, accepted, 0)

def average(attempts: list):
    def grade_summer(cr_sum, attempt):
        return cr_sum + attempt.grade 
    accepted = list(filter(lambda s: s.grade > 0, attempts))
    sum_of_grades = reduce(grade_summer, accepted, 0)
    return sum_of_grades / len(accepted)
"""