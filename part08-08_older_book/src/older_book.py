class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

def older_book(book1: Book, book2: Book):
    olderbook = book1 if book1.year < book2.year else book2
    if book1.year == book2.year:
        print(f'{book1.name} and {book2.name} were published in {book1.year}')
    else:
        print(f'{olderbook.name} is older, it was published in {olderbook.year}') 