from os import getlogin
import sys


def get_name(filename):
    username = getlogin()
    given_name = input(f"give me your name {username}: ")

    with open(filename, "w") as created_file:
        created_file.write(username)
        created_file.write(given_name)


if __name__ == "__main__":
    p_filename = sys.argv[1]
    get_name(p_filename)
