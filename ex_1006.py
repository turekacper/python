def get_numbers():
    i = 1
    numbers = []
    while True:
        number = input(f"Number {i}: ")
        i += 1
        if number == "q":
            return numbers
        try:
            number_int = int(number)
        except ValueError:
            print("The input must be a number, not text.")
        else:
            numbers.append(number_int)


def addition(numbers):
    result_sum = 0
    for i in numbers:
        result_sum += i
    print(result_sum)


addition(get_numbers())
