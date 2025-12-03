from os import getlogin
import sys


def get_name():
    user_login = getlogin()
    while True:
        given_name = input(
            f" To quit press 'q'. \n Hello {user_login}. Give me your name: "
        )
        if given_name == "q":
            break
        with open("zapis_imion3.txt", "a") as name_file:
            name_file.write(given_name + "\n")


if __name__ == "__main__":
    get_name()
