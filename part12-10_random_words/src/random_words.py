from random import randint


def word_generator(characters: str, length: int, amount: int):
    for i in range(amount):
        word = ''
        for j in range(length):
            word += characters[randint(0, len(characters)-1)]
        yield word

"""
from random import choice

def word_generator(letters: str, length: int, amount:int):
    return ("".join([choice(letters ) for i in range(length)]) for j in range(amount))
"""