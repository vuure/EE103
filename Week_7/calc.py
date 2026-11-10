def calculator(operation,x,y):
    if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float):
        if operation == "add":
            return add(x,y)
        elif operation == "subtract":
            return subtract(x,y)
        elif operation == "multiply":
            return multiply(x,y)
        elif operation == "divide":
            if y == 0:
                return "Type Error: Denominator cannot be zero."
            else:
                return divide(x,y)
        else:
            return "Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
    return x,y,type(x),type(y)

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y