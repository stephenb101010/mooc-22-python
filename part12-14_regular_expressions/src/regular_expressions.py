import re

def is_dotw(my_string: str):
    if re.search('Mon|Tue|Wed|Thu|Fri|Sat|Sun', my_string):
        return True
    return False

def all_vowels(my_string: str):
    if re.search('^[aeiouy]*$', my_string):
        return True
    return False

def time_of_day(my_string: str):
    if re.search('([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', my_string):
        return True
    return False

"""
def is_dotw(my_string: str):
    return re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string) is not None

def all_vowels(my_string: str):
    return re.search("^[aeiouy]*$", my_string) is not None

def time_of_day(my_string: str):
    return re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string) is not None
"""