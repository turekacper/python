import json
from os import getlogin


def get_number():
    filename = getlogin() + "_fav_numer.json"
    while True:
        try:
            fav_number = int(input("Give me your favorite number: "))
            p_fav_number = fav_number
            number_in_file = check_number(filename)
            print(number_in_file)
            if fav_number == number_in_file:
                print("Liczba jest ta sama")
                continue
            else:
                break
        except ValueError:
            print("Give me a number not a string")
    with open(filename, "w") as file_obj:
        json.dump(fav_number, file_obj)


def read_file(filename):
    try:
        with open(filename) as file_obj:
            fav_number = json.load(file_obj)
            print("Your favorite number is : " + str(fav_number))

    except FileNotFoundError:
        print("File not found")


def check_number(filename):
    try:
        with open(filename) as file_obj:
            fav_number = json.load(file_obj)
    except FileNotFoundError:
        print("File not found")
        return 0

    return fav_number


if __name__ == "__main__":
    #    read_file(getlogin() + "_fav_numer.json")
    get_number()
