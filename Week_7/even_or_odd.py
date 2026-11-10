def evenOrOdd(num):
    if isinstance(num, (int)):
        num = int(num)
        if int(num) % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Invalid input"