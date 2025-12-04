from os import getlogin

# function for getting filenames


def get_files_names():
    filename_cats_len = 0
    filename_cats = ""
    filename_dogs_len = 0
    filename_dogs = ""
    while filename_cats_len == 0:
        filename_cats = input(
            f"Hello {getlogin()}, give me filename for names of cats:"
        )

        filename_cats_len = len(filename_cats)
        if filename_cats_len == 0:
            print("You didn't give filename for cats.")
    while filename_dogs_len == 0:
        filename_dogs = input(
            f"Hello {getlogin()}, give me filename for names of dogs:"
        )

        filename_dogs_len = len(filename_dogs)
        if filename_dogs_len == 0:
            print("You didn't give filename for dogs.")
    return filename_cats, filename_dogs


def read_files():
    cat_file, dog_file = get_files_names()
    print(cat_file)
    print(dog_file)
    try:
        with open(cat_file) as file_object:
            cat_names = file_object.read()
            print(cat_names)
    except FileNotFoundError:
        print("nie znaleziono pliku z kotkami")
    try:
        with open(dog_file) as file_object2:
            dog_names = file_object2.read()
            print(dog_names)
    except FileNotFoundError:
        print("nie znaleziono pliku z psami")


if __name__ == "__main__":
    read_files()
