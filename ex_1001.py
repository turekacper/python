def read_whole_file(string):
    with open(string) as opened_file:
        text = opened_file.read()
    print(text)


def print_looped(string):
    with open(string) as opened_file:
        for line in opened_file:
            print(line.rstrip())


def open_list(string):
    with open(string) as opened_file:
        text_list = opened_file.readlines()
    for i in text_list:
        print(i.rstrip())


def replace_string(string):
    with open(string) as opened_file:
        text = opened_file.read().replace("python", "C language")
        print(text)


read_whole_file("ex_1001.txt")
open_list("ex_1001.txt")
print_looped("ex_1001.txt")
replace_string("ex_1001.txt")
