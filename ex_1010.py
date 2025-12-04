from itertools import groupby


def read_book(book_title):
    try:
        with open(book_title + ".txt") as file_object:
            book = file_object.read()
            book_words = book.split()
            for word, group in groupby(book_words):
                print(f"{word}: {len(list(group))}")
    except FileNotFoundError:
        print("Podany zly tytul ksiazki")


if __name__ == "__main__":
    print(read_book("book"))
