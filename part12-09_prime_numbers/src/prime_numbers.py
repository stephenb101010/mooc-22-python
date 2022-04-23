def is_prime(number: int):
    for i in range(2, number):
        if number%i == 0:
            return False
    return True

def prime_numbers():
    i = 1
    while True:
        i += 1
        if is_prime(i):
            yield i

"""
def prime_numbers():
    number = 1
    while True:
        if is_prime(number):
            yield number
        number += 1
 
# Helper method for checking if number is prime
def is_prime(number: int):
    if number < 2:
        return False
    # Possible divisor is between 2 and number-1
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
"""