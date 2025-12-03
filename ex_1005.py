from os import getcwd, getlogin
import sys


def get_answer_programming():
    while True:
        cwd = getcwd()
        why_programming = input(
            f"Hello {getlogin()}. Give me the reason yoy like programming: "
        )
        with open("1005.txt", "a") as file:
            file.write(why_programming + "\n")
            file.write(" " + cwd)
        if why_programming == "no":
            break


if __name__ == "__main__":
    get_answer_programming()
