def even_numbers(beginning: int, maximum: int):
    while beginning <= maximum:
        if beginning%2 == 0:
            yield beginning
        beginning += 1