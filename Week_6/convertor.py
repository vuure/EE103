def binary_convertor(number):
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2

    return binary